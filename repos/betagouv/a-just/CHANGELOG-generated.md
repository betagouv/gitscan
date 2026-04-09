## Changelog : a-just (30 derniers jours, au 9 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur, notamment la visualisation des données et la gestion des stocks à vérifier. Des corrections ont également été apportées concernant l'importation des agents EAM et la gestion des dates. Enfin, une mise à jour importante des dépendances a été effectuée pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Correction de la visualisation des dernières données dans le cockpit [#21721ffd](https://github.com/betagouv/a-just/commit/21721ffd).
- Amélioration de la propagation des stocks à vérifier lors de la confirmation [#90bb2290](https://github.com/betagouv/a-just/commit/90bb2290) et [#459dda1c](https://github.com/betagouv/a-just/commit/459dda1c).
- Ajout d'infobulles (tooltips) pour les informations d'alerte dans les commentaires des agents [#f7580e9f](https://github.com/betagouv/a-just/commit/f7580e9f).
- Correction de l'importation des agents EAM [#b4fd2ea5](https://github.com/betagouv/a-just/commit/b4fd2ea5).
- Correction de la date de fin d'historique [#278e5e5f](https://github.com/betagouv/a-just/commit/278e5e5f).
- Correction des CGU [#fe3bbe68](https://github.com/betagouv/a-just/commit/fe3bbe68).

### Évolutions techniques
- Mise à jour des dépendances Node.js, PostgreSQL, Angular, TypeScript et autres librairies pour améliorer la sécurité et la performance [#31e23169](https://github.com/betagouv/a-just/commit/5fe23169), [#fa9f6da3](https://github.com/betagouv/a-just/commit/fa9f6da3), [#ba026483](https://github.com/betagouv/a-just/commit/ba026483), [#45bc70b0](https://github.com/betagouv/a-just/commit/45bc70b0), [#1f718ef3](https://github.com/betagouv/a-just/commit/1f718ef3), [#dcb986a5](https://github.com/betagouv/a-just/commit/dcb986a5), [#6d674dc8](https://github.com/betagouv/a-just/commit/6d674dc8), [#91d72dc4](https://github.com/betagouv/a-just/commit/91d72dc4), [#d9ec52dc](https://github.com/betagouv/a-just/commit/d9ec52dc), [#46ff8a3b](https://github.com/betagouv/a-just/commit/46ff8a3b), [#109c928b](https://github.com/betagouv/a-just/commit/109c928b).
- Refonte de la gestion des erreurs Koa avec la création d'un `koa-smart` personnalisé [#47452fac](https://github.com/betagouv/a-just/commit/47452fac) et [#bc0abba9](https://github.com/betagouv/a-just/commit/bc0abba9).
- Suppression de Compodoc et remplacement par des scripts en ligne [#d412ca33](https://github.com/betagouv/a-just/commit/d412ca33) et [#8604534d](https://github.com/betagouv/a-just/commit/8604534d).
- Suppression de precommit [#1f199636](https://github.com/betagouv/a-just/commit/1f199636).

### Autres changements
- Suppression de la documentation temporaire [#9017c45d](https://github.com/betagouv/a-just/commit/9017c45d).
- Suppression du formatage des dates [#109c928b](https://github.com/betagouv/a-just/commit/109c928b).
- Corrections et mises à jour de la configuration de construction (build) et des scripts associés [#23e547fd](https://github.com/betagouv/a-just/commit/23e547fd), [#92bc178e](https://github.com/betagouv/a-just/commit/92bc178e), [#be412a02](https://github.com/betagouv/a-just/commit/be412a02), [#1db0b5ba](https://github.com/betagouv/a-just/commit/1db0b5ba), [#ca5f6acd](https://github.com/betagouv/a-just/commit/ca5f6acd), [#3b78c893](https://github.com/betagouv/a-just/commit/3b78c893), [#5e54ffc2](https://github.com/betagouv/a-just/commit/5e54ffc2), [#5aee2964](https://github.com/betagouv/a-just/commit/5aee2964), [#3e4979ac](https://github.com/betagouv/a-just/commit/3e4979ac), [#d45eabfc](https://github.com/betagouv/a-just/commit/d45eabfc), [#19898990](https://github.com/betagouv/a-just/commit/19898990), [#e5c76048](https://github.com/betagouv/a-just/commit/e5c76048), [#5111a177](https://github.com/betagouv/a-just/commit/5111a177).
- Suppression du nombre aléatoire pour la sécurité des mots de passe [#24c8608f](https://github.com/betagouv/a-just/commit/24c8608f).
- Modification de l'affectation des ATJ [#34925316](https://github.com/betagouv/a-just/commit/34925316).
