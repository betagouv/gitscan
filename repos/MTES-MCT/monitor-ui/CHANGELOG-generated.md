## Changelog : monitor-ui (30 derniers jours)

### Résumé
Les récentes mises à jour de monitor-ui se concentrent principalement sur l'amélioration des performances et la correction de bugs, notamment au niveau du composant "check tree picker". Des améliorations de l'interface utilisateur et des corrections de bugs mineurs ont également été apportées, ainsi que des ajouts d'icônes et de couleurs réglementaires.

### Évolutions fonctionnelles
- Correction d'un bug dans le composant `DatePicker` qui empêchait la fermeture correcte des calendriers en cliquant en dehors. [#64740cc](https://github.com/MTES-MCT/monitor-ui/commit/64740ccf300e0f697a447b2db122807ebbf3cf18)
- Amélioration des performances du composant `check tree picker` grâce à un rendu paresseux des options et à l'ajout d'un debounce pour la recherche.
- Ajout d'icônes pour les onglets des navires. [#19d2fc9](https://github.com/MTES-MCT/monitor-ui/commit/19d2fc9040b8d28c2cfe0cc0518514e882a76e75)
- Ajout d'une nouvelle icône "Copier". [#d717e9f](https://github.com/MTES-MCT/monitor-ui/commit/d717e9f5103750ca56f8cf276e5bb68293bf95a8)
- Ajout de nouvelles couleurs réglementaires. [#c3f5ca4](https://github.com/MTES-MCT/monitor-ui/commit/c3f5ca48b83c04694cf77a81cd7e25fac0cb0481)

### Évolutions techniques
- Correction du type de retour de la fonction `onChange` dans le composant `check tree picker`. [#eb6a504](https://github.com/MTES-MCT/monitor-ui/commit/eb6a504b618be999f3e539c645a1741eadd5b890)
- Ajout de tests unitaires pour le composant `check tree picker`. [#ade5b29](https://github.com/MTES-MCT/monitor-ui/commit/ade5b299612544019f6826704619684393581674)
- Refactoring du composant `MultiZoneEditor` renommé en `MultiLocationEditor` avec modification des props. [#c41b601](https://github.com/MTES-MCT/monitor-ui/commit/c41b60112a702e5f3097d5a964f1940198999364)
- Mise en place de variables d'environnement pour la gestion des tokens NPM. [#626ac09](https://github.com/MTES-MCT/monitor-ui/commit/626ac095ce23dc05b48cb8be3330d5416c0f2ee7) et [#eee2b56](https://github.com/MTES-MCT/monitor-ui/commit/eee2b566c882a0da9f4823439b651641d9b73575)

### Autres changements
- Correction d'un bug de comparaison dans le composant `check tree picker`. [#8bf8dd9](https://github.com/MTES-MCT/monitor-ui/commit/8bf8dd90712477f84e5982443402fc5f9a74d8ce)
- Vérification de la présence du fichier `.npmrc`. [#a5f3b56](https://github.com/MTES-MCT/monitor-ui/commit/a5f3b5645d6)
