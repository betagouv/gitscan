## Changelog : mobilic-api (30 derniers jours, au 08 mai 2026)

### Résumé
Ce mois-ci, l'API Mobilic a bénéficié d'améliorations significatives en matière de sécurité avec l'implémentation de l'authentification à deux facteurs (TOTP) et de la gestion de l'usurpation d'identité. Des corrections ont également été apportées à la gestion des fuseaux horaires dans les exports et à la gestion des noms dans les envois d'emails Brevo. L'interface administrateur a été remaniée et des recherches avancées sur les NATINF ont été ajoutées.

### Évolutions fonctionnelles
- **Authentification:** Ajout de la prise en charge de l'authentification à deux facteurs (TOTP) avec génération de code via application mobile. [#694](https://github.com/MTES-MCT/mobilic-api/issues/694)
- **Interface Administrateur:** Refonte de la page d'accueil de l'interface administrateur pour une meilleure expérience utilisateur. [#698](https://github.com/MTES-MCT/mobilic-api/issues/698)
- **Recherche NATINF:** Possibilité de rechercher des NATINF personnalisés via l'API. [#700](https://github.com/MTES-MCT/mobilic-api/issues/700)
- **Exports:** Correction de l'application des fuseaux horaires dans les exports et les PDF. [#671](https://github.com/MTES-MCT/mobilic-api/issues/671)
- **Alertes réglementaires:** Enrichissement des alertes réglementaires avec des informations sur le jour et l'ID utilisateur.
- **Tableau de bord:** Ajout d'une nouvelle requête GraphQL pour obtenir un résumé du tableau de bord.
- **Support Admin:** Amélioration du support administrateur avec la possibilité d'usurper l'identité d'un utilisateur. [#685](https://github.com/MTES-MCT/mobilic-api/issues/685)

### Évolutions techniques
- **Sécurité:**
    - Ajout d'une journalisation d'audit pour l'usurpation d'identité.
    - Blocage de l'usurpation d'identité sur soi-même et sur les administrateurs.
    - Ajout de tests de sécurité pour la détection d'IDOR et d'autres vulnérabilités.
    - Limitation de la complexité des requêtes GraphQL pour prévenir les attaques par déni de service (DoS).
    - Désactivation de GraphiQL en production pour des raisons de sécurité.
- **Refactoring:**
    - Simplification du code lié aux alertes réglementaires pour réduire la complexité cognitive.
    - Déduplication de requêtes pour les emails d'activation.
    - Centralisation de fonctions pour éviter la duplication de code.
- **Infrastructure:** Mise à jour de pipenv en CircleCI.

### Autres changements
- Correction de l'ordre des révisions de migrations.
- Correction de la gestion des noms dans les envois d'emails Brevo.
- Ajout d'un utilisateur super-administrateur dans les seeds.
- Suppression du contexte des accès aux données d'activité.
- Correction de bugs mineurs et améliorations de la documentation.
