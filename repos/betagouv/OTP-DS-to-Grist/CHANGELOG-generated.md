## Changelog : OTP-DS-to-Grist (30 derniers jours, au 11 septembre 2026)

### Résumé
Cette période a été marquée par l'amélioration de la précision des données exportées grâce à l'introduction de filtres multiples et la correction de problèmes d'affichage dans les tableaux. Le projet a également bénéficié d'un nettoyage important du code et d'une optimisation des processus de synchronisation pour gagner en stabilité.

### Évolutions fonctionnelles
- Ajout de la gestion de filtres multiples pour affiner l'exportation des données ([#459](https://github.com/betagouv/OTP-DS-to-Grist/issues/459))
- Amélioration de la section d'aide (mise à jour des liens et support des variables d'environnement) ([#487](https://github.com/betagouv/OTP-DS-to-Grist/issues/487))
- Correction de l'affichage des blocs répétables (suppression des colonnes vides dans la table des champs) ([#468](https://github.com/betagouv/OTP-DS-to-Grist/issues/468))

### Évolutions techniques
- Optimisation de la synchronisation automatique : suppression de routes inutilisées et renforcement de la couverture de tests ([#478](https://github.com/betagouv/OTP-DS-to-Grist/issues/478))
- Refactoring du code : extraction de la classe `ColumnCache` pour une meilleure modularité ([#472](https://github.com/betagouv/OTP-DS-to-Grist/issues/472))
- Nettoyage technique : suppression de code mort et maintenance des agents ([#477](https://github.com/betagouv/OTP-DS-to-Grist/issues/477), [#501](https://github.com/betagouv/OTP-DS-to-Grist/issues/501))

### Autres changements
- Documentation : suppression du fichier `technique.md`
