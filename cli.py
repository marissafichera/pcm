# ===============================================================================
# Copyright 2021 ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--template', default=None, help='Device Template to use. Typically the device models name')
@click.argument('name')
def device(template, name):
    click.echo('Create a new device configuration')


@cli.command()
@click.option('--app', default=None, help='Application style to install. pycrunch, pyexperiment,...')
def install():
    click.echo('Install the pychron application')


@cli.command()
@click.argument('name')
def script(name):
    click.echo('script, {}'.format(name))
    




if __name__ == '__main__':
    cli()
# ============= EOF =============================================
