## Changelog : api-subventions-asso (30 derniers jours)

### Résumé
Ce mois-ci, l'API a bénéficié d'améliorations significatives en termes de performance, notamment lors de l'importation de fichiers Chorus. Des corrections de bugs ont été apportées pour améliorer la robustesse de l'application, en particulier concernant le parsing des fichiers SCdL et la gestion des données SIREN/RNA. De nouvelles fonctionnalités ont été ajoutées pour faciliter le suivi des données et améliorer la transparence, comme l'export de données vers Metabase.

### Évolutions fonctionnelles
- Amélioration de la performance lors de l'importation de fichiers Chorus (#3809).
- Ajout d'informations sur l'administrateur dans les données de suivi (datalog) (#3813).
- Correction d'un bug qui empêchait la détection correcte des plages de données dans les fichiers XLSX (#3801).
- Correction d'un problème lié à la gestion des numéros SIREN/RNA multiples et indéfinis (#3797).
- Troncature des numéros SIRET multiples dans l'interface utilisateur (#3798).
- Export des données de datalog vers Metabase pour une meilleure analyse (#3796).
- Ajout d'un mécanisme de "debouncing" pour les notifications de perte de connexion (#3810).

### Évolutions techniques
- Refactorisation du code pour améliorer la modularité et la maintenabilité, notamment au niveau des services "plats" (#3815).
- Refactorisation et documentation améliorée de la logique de recherche SIREN/RNA (#3787).
- Mise à jour de la configuration TypeScript (#3799).
- Amélioration de la gestion des écritures en masse dans la base de données pour éviter les erreurs (#3801, #3780).
- Utilisation de `rimraf` à la place de `rm -rf` dans les scripts pour une meilleure compatibilité (#3776).
- Refactorisation du mapper, du port et de l'adaptateur (#3828).
- Ajout de statistiques détaillées sur les consommateurs de l'API (#3826).

### Autres changements
- Correction d'un bug empêchant l'écriture en masse lorsque qu'il n'y avait pas de documents à mettre à jour.
- Publication des versions v0.78.0 et v0.78.1.
