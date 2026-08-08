## Changelog : data_pass (30 derniers jours, au 06/08/2026)

### Résumé
Les récentes évolutions se concentrent sur l'élargissement de l'offre de formulaires (notamment pour les cantines et les API particuliers), l'amélioration de la clarté de l'interface lors de l'instruction des dossiers et le renforcement de la sécurité de l'application.

### Évolutions fonctionnelles
- **Nouveaux éditeurs et formulaires** : intégration de l'éditeur Ianord (formulaires cantines) [#1710](https://github.com/etalab/data_pass/issues/1710), de l'éditeur Hoptis Software (API Particulier) [#1690](https://github.com/etalab/data_pass/issues/1690), des formulaires EAJE et des aides CNAV (rentrée scolaire).
- **Expérience utilisateur** : passage des formulaires d'instruction en mode consultation (retrait des boutons de modification et du panneau latéral) pour une meilleure lisibilité [#1701](https://github.com/etalab/data_pass/issues/1701), ajout de fil d'Ariane et création d'une interface pour visualiser les emails automatisés.
- **Clarté des données** : amélioration de l'explication des rôles et des niveaux de droits dans les interfaces de gestion, et ajout d'un label "statut de la demande".
- **Corrections** : résolution de problèmes liés à la proactivité CNOUS, à la suppression involontaire de droits et à la gestion des identifiants FranceConnect.

### Évolutions techniques
- **Sécurité** : mise à jour de Rails pour corriger la vulnérabilité CVE-2026-66066 [#1715](https://github.com/etalab/data_pass/issues/1715) et restriction du périmètre d'accès (scope) OAuth pour HubEE, passant de `ADMIN` à `DATAPASS` [#1724](https://github.com/etalab/data_pass/issues/1724).
- **Infrastructure et Observabilité** : passage à la production de journaux au format JSON via logstasher [#1714](https://github.com/etalab/data_pass/issues/1714) et suppression des configurations d'environnement locales au profit d'une gestion centralisée par Ansible.
- **Refactoring** : refonte, factorisation et uniformisation des cadres juridiques pour les formulaires "API Particulier" [#1605](https://github.com/etalab/data_pass/issues/1605).
- **Authentification** : ajout du scope INE.

### Autres changements
- **Documentation et libellés** : affinement des textes et des formulations suite aux retours du pôle juridique et mise à jour des introductions pour les services CISIRH.
