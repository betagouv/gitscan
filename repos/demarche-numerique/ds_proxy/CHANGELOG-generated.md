## Changelog : ds_proxy (30 derniers jours, au 27 mars 2026)

### Résumé
Les récentes évolutions de ds_proxy se concentrent sur l'amélioration de la gestion des mots de passe, la simplification du processus de construction des images Docker et l'ajout d'informations sur les tags lors de l'appel de la commande `--version`. Ces changements visent à faciliter l'utilisation et la maintenance du proxy.

### Évolutions fonctionnelles
- La commande `--version` affiche désormais les tags disponibles, offrant une meilleure identification des versions. [#141](https://github.com/demarche-numerique/ds_proxy/pull/141)
- Correction d'un bug dans la gestion des mots de passe : l'écriture d'un mot de passe dans un fichier ne génère plus de nouvelle ligne à la fin. [#143](https://github.com/demarche-numerique/ds_proxy/pull/143)

### Évolutions techniques
- Refonte du processus de construction des images Docker pour simplifier la création d'images à partir de packages. [#142](https://github.com/demarche-numerique/ds_proxy/pull/142)
- Ajout d'une vérification de l'image Docker dans le workflow CI avant la fusion des modifications.
- Renommage des fichiers Docker pour plus de clarté.

### Autres changements
- Mise à jour des dépendances du projet. [#141](https://github.com/demarche-numerique/ds_proxy/pull/141)
