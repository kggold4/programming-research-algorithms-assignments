from inspect import getmembers, isfunction
import importlib
import sys


def save_html_file(file_name, output):
    html_file = open(file_name, 'w')
    html_file.write(output)
    html_file.close()
    print('file created')


def get_title(title_text: str):
    return f'<span style="color:blue;font-style:italic;">{title_text} </span>'


def create_html_file(module_name: str, out_html_file: str):
    # help from: https://stackoverflow.com/questions/8718885/import-module-from-string-variable
    module = importlib.import_module(module_name.replace('.py', ''))
    output_html = f'<head><h1>{get_title("File Documentation:")}{module.__doc__}</h1><br>'

    # help from: https://stackoverflow.com/questions/139180/how-to-list-all-functions-in-a-python-module#:~:text=The%20Python%20documentation%20provides%20the,the%20functions%20within%20that%20module.
    for func in getmembers(module, isfunction):
        output_html += f'<h2>{get_title("Function name:")}{module.__getattribute__(func[0]).__name__}</h2>'
        output_html += f'<h4>{get_title("Function Documentation:")}{module.__getattribute__(func[0]).__doc__}</h4>'
        output_html += f'<p>{get_title("Function Annotations:")}{module.__getattribute__(func[0]).__annotations__}</p>'
        output_html += '<br>'

    output_html += '</head>'
    save_html_file(file_name=out_html_file, output=output_html)


def main():
    # help from https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1204/handouts/py-main.html
    args = sys.argv[1:]
    print(args)
    create_html_file(module_name=args[0], out_html_file=args[1])


if __name__ == '__main__':
    main()
