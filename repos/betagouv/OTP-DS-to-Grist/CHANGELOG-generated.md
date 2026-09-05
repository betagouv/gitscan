## Changelog : OTP-DS-to-Grist (30 derniers jours, au 03 septembre 2026)

### Résumé
Ce mois-ci, le projet s'est concentré sur l'amélioration de la précision des données et de l'expérience utilisateur, notamment grâce à l'introduction de filtres multiples et à la correction de problèmes liés aux champs répétables. Une phase importante de nettoyage et de refactorisation a également été menée pour assainir le code et améliorer sa maintenabilité.

### Évolutions fonctionnelles
- Ajout de la possibilité d'utiliser plusieurs filtres simultanément ([#459](https://github.com/betagouv/OTP-DS-to-Grist/issues/459)).
- Correction de la gestion des blocs répétables pour éviter l'apparition de colonnes vides dans la table des champs ([#468](https://github.com/betagouv/OTP-DS-to-Grist/issues/468)).
- Stabilisation du suffixe utilisé pour identifier les doublons de champs ([#460](https://github.com/betagouv/OTP-DS-to-Grist/issues/460)).
- Travaux de recherche (POC) pour permettre la récupération de l'adresse email des utilisateurs ([#435](https://github.com/betagouv/OTP-DS-to-Grist/issues/435)).

### Évolutions techniques
- Refactorisation de la gestion du cache des colonnes via l'extraction d'une classe dédiée `ColumnCache` ([#472](https://github.com/betagouv/OTP-DS-to-Grist/issues/472)).
- Nettoyage du projet par la suppression de code mort et de routes inutilisées ([#477](https://github.com/betagouv/OTP-DS-to-Grist/issues/477), [#478](https://github.com/betagouv/OTP-DS-to-Grist/issues/478)).

### Autres changements
- Mise à jour des liens d'aide et passage par des variables d'environnement pour la configuration ([#487](https://github.com/betagouv/OTP-DS-to-Grist/issues/487)).
- Nettoyage de la documentation (suppression de `technique.md`).
