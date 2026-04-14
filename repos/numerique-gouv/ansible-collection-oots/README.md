# Ansible Collection - betagouv.oots

This collection of Ansible roles aims at helping set up the software that can be
used by any European Union Member State in order to participate to the
[Only-Once Technical
System](https://ec.europa.eu/digital-building-blocks/sites/display/OOTS/About+OOTS)
(OOTS).

## Important security considerations

Some roles are provided with default settings that may allow you run functional
software, but some parameters such as private keys, passwords and privileged
accounts must be changed in order to run them safely in a production
environment.

## How to install

This collection can be installed and its roles can be integrated to Ansible
playbooks.

Add the following to your Ansible Galaxy `requirements.yml` file:

```yaml
collections:
  - name: https://github.com/numerique-gouv/ansible-collection-oots.git
    type: git
```

You can then install it with the command:

    ansible-galaxy collection install -r requirements.yml

You will then be able to call on the roles of this collection using the name
`betagouv.oots.<role_name>`.

## Roles documentation

All available roles are in the folder `roles` and each role is documented in
detail under its `meta/argument_specs.yml` file.
