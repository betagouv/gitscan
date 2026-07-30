## Changelog : portail-rse (30 derniers jours, au 23 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la VSME (Valeur Sociale Mesurée Environnementale) avec des améliorations significatives de l'exportation des rapports au format PPTX et XLSX, ainsi que des corrections de bugs et des optimisations. Des améliorations de la sécurité et de l'expérience utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de l'UX de la modale d'export [#f65c820](https://github.com/betagouv/portail-rse/commit/f65c820)
- Possibilité de réinitialiser un indicateur VSME [#2a12381](https://github.com/betagouv/portail-rse/commit/2a12381)
- Fourniture d'un rapport d'exemple VSME [#1a28323](https://github.com/betagouv/portail-rse/commit/1a28323)
- Les exports PPTX et XLSX de la VSME sont maintenant logués pour faciliter le débogage [#260e6ff](https://github.com/betagouv/portail-rse/commit/260e6ff)
- Correction du label d'une colonne de l'indicateur B7-38-c [#effe076](https://github.com/betagouv/portail-rse/commit/effe076)
- Correction de l'export PPTX de l'indicateur C3-54-p2 dans les cas non pertinents et non applicables [#4d589ee](https://github.com/betagouv/portail-rse/commit/4d589ee)
- Amélioration de la recherche d'utilisateurs dans l'administration par ensemble d'ID [#0b826a1](https://github.com/betagouv/portail-rse/commit/0b826a1)

### Évolutions techniques
- Mise à jour de Django de la version 5.1.15 à la version 5.2.16 [#48eb2fc](https://github.com/betagouv/portail-rse/commit/48eb2fc)
- Mise à jour de Node.js dans `package.json` et dans l'intégration continue [#376ab90](https://github.com/betagouv/portail-rse/commit/376ab90)
- Refactoring de la définition d'un attribut dans l'administration [#8adeba0](https://github.com/betagouv/portail-rse/commit/8adeba0)
- Correction d'un problème où un champ calculé pouvait provoquer des erreurs de validation [#d167f46](https://github.com/betagouv/portail-rse/commit/d167f46)
- Correction du type d'un champ calculé dans la VSME [#106119a](https://github.com/betagouv/portail-rse/commit/106119a)
- Refactoring du code d'export PPTX de la VSME pour une meilleure homogénéité et suppression de code dupliqué [#7c14d36](https://github.com/betagouv/portail-rse/commit/7c14d36), [#3ca1740](https://github.com/betagouv/portail-rse/commit/3ca1740), [#985ebfb](https://github.com/betagouv/portail-rse/commit/985ebfb)

### Autres changements
- Nettoyage du compte utilisateur de test et restriction des modifications de profil et de mot de passe pour plus de sécurité [#f910a2b](https://github.com/betagouv/portail-rse/commit/f910a2b), [#4df6290](https://github.com/betagouv/portail-rse/commit/4df6290), [#42bcad5](https://github.com/betagouv/portail-rse/commit/42bcad5)
- Renommage d'une commande pour refléter son action élargie [#b5f630c](https://github.com/betagouv/portail-rse/commit/b5f630c)
- Correction d'un bug où les données pouvaient être vides dans un tableau PPTX avec un nombre de lignes variable [#6824421](https://github.com/betagouv/portail-rse/commit/6824421)
- Refactoring et renommage de méthodes dans la VSME [#8c5ae53](https://github.com/betagouv/portail-rse/commit/8c5ae53), [#6274b2a](https://github.com/betagouv/portail-rse/commit/6274b2a)
- Correction d'un problème où l'export PPTX pouvait échouer si un schéma avait été supprimé [#6274b2a](https://github.com/betagouv/portail-rse/commit/6274b2a)
