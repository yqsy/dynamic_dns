from setuptools import setup


setup(
    name="dynamic_dns",
    version="1.0.0",
    license='http://www.apache.org/licenses/LICENSE-2.0',
    description="ali DNS dynamic update",
    author='yqsy021',
    author_email='yqsy021@126.com',
    url='https://github.com/yqsy/dynamic_dns',
    packages=['dynamic_dns'],
    install_requires=['aliyun-python-sdk-domain>=3.0.1',
                      'schedule>=0.5.0'],
    entry_points="""
    [console_scripts]
    dynamic_dns = dynamic_dns.dynamic_dns:main
    """,
)
