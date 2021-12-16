from app.templates.controllers.controller import ControllerBase
from flask import render_template, request, flash
from calc.calculator import Calculator


class IndexController(ControllerBase):
    """values can be entered """

    @staticmethod
    def post():
        """ get the numbers entered """

        nums = [int(num) for num in request.form["nums"].split()]

        if len(nums) < 2:
            flash('You need to calculate at least 2 numbers', category="danger")
        else:
            flash('Successfully calculated', category="success")

            operation = request.form['operation']

            Calculator.calculate_numbers(operation, *nums)
            result = str(Calculator.get_calculation_last())

            return render_template('results.html', operation=operation, nums=nums, result=result)
        return render_template("calculator2.html")

    @staticmethod
    def get():
        """ calculator page """
        return render_template('calculator2.html')
