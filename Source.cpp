//var 2
#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

void metod_teylora(double h, double *y, double *dy) {
	int n = 2 / h;

	double* x = new double[n];
	for (int i = 0; i < n; i++)
		x[i] = i*h;

	y[0] = 1;
	dy[0] = 0;
	double d2y = -1;
	double d3y = -1;
	double d4y = 6;
	for (int i = 1; i < n; i++) {
		y[i] = y[i - 1] + h*dy[i - 1] + h*h*d2y / 2. + h*h*h*d3y / 6.;
		dy[i] = dy[i - 1] + h*d2y + h*h*d3y / 2. + h*h*h*d4y / 6.;
		d2y = cos(x[i])*exp(-2 * x[i]) - dy[i] - 2 * y[i];
		d3y = exp(-2 * x[i])*(-2 * cos(x[i]) - sin(x[i])) - d2y - 2 * dy[i];
		d4y = exp(-2 * x[i])*(3 * cos(x[i]) + 4 * sin(x[i])) - d3y - 2 * d2y;
	}
}

double opt_h(double eps = 0.01) {
	double h = 1;
	bool conv = true;
	do {
		int n = 2 / h;
		double * y = new double[n];
		double *dy = new double[n];
		metod_teylora(h, y, dy);
		h /= 2;
		double *y1 = new double[2 * n];
		double *dy1 = new double[2 * n];
		metod_teylora(h, y1, dy1);

		double delta_y = abs(y[0] - y1[0]);
		double delta_dy = abs(dy[0] - dy1[0]);

		for (int i = 0; i < n; i++) {
			if (delta_y < abs(y[i] - y1[2 * i])) {
				delta_y = abs(y[i] - y1[2 * i]);
			}
			if (delta_dy < abs(dy[i] - dy1[2 * i])) {
				delta_dy = abs(dy[i] - dy1[2 * i]);
			}
		}
		conv = delta_y >= eps || delta_dy >= eps;
	} while (conv);
	return h;
}

int main()
{
	double h = opt_h();
	cout << "h = " << h << endl;
	int n = 2 / h;
	double *y = new double[n];
	double *dy = new double[n];
	y[0] = 1;
	dy[0] = 0;
	metod_teylora(h, y, dy);

	ofstream out("sol.txt", ios_base::out);

	for (int i = 0; i < n; i++) {
		out << y[i] << "," << dy[i] << "," << i*h << endl;
	}
	out.close();
	return 0;
}
