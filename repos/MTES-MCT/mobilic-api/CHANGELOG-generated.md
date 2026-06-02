## Changelog : mobilic-api (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la sécurité avec l'ajout de l'authentification à deux facteurs (TOTP), la refonte de l'espace administrateur pour une meilleure visibilité des données, et l'ajout de fonctionnalités de support et d'audit. Des corrections de bugs et des améliorations de la gestion des données ont également été apportées.

### Évolutions fonctionnelles
- **Authentification:** Ajout de l'authentification à deux facteurs (TOTP) pour une sécurité renforcée. Les utilisateurs peuvent désormais configurer et utiliser des codes TOTP pour se connecter. [#685](https://github.com/MTES-MCT/mobilic-api/pulls/685)
- **Espace Administrateur:** Refonte de la page d'accueil de l'espace administrateur avec de nouveaux indicateurs et des informations plus précises sur les données clés. [#698](https://github.com/MTES-MCT/mobilic-api/pulls/698)
- **Support Admin:** Ajout de fonctionnalités permettant à l'administration de supporter un utilisateur en se mettant à son compte. [#685](https://github.com/MTES-MCT/mobilic-api/pulls/685)
- **Contrôles:** Ajout de l'information `isCTT` aux informations utilisateur disponibles dans l'interface de contrôle. [#700](https://github.com/MTES-MCT/mobilic-api/pulls/700)
- **Notifications:** Implémentation de rappels par email pour l'activation du compte utilisateur. [#697](https://github.com/MTES-MCT/mobilic-api/pulls/697)
- **Téléchargement CGU:** Correction d'un problème empêchant le téléchargement des CGU pour les données personnelles. [#702](https://github.com/MTES-MCT/mobilic-api/pulls/702)

### Évolutions techniques
- **Sécurité:** Ajout d'un audit pour l'impersonation d'utilisateurs, incluant la journalisation des actions et des mécanismes de protection contre les abus.
- **Refactoring:** Déduplication des requêtes pour les rappels d'activation afin d'optimiser les performances.
- **Architecture:** Utilisation du claim `impersonate_as` dans les JWT pour gérer l'impersonation d'utilisateurs, remplaçant l'ancien cookie `admin_token`.
- **Base de données:** Correction de l'ordre des révisions de migrations pour assurer la cohérence de la base de données.
- **Code:** Centralisation d'une fonction dans le module de contrôle pour éviter la duplication de code.

### Autres changements
- Ajout d'un support pour la création d'un super-administrateur via la seed.
- Ajout de tests unitaires et d'intégration pour la sécurité, notamment pour la protection contre les attaques IDOR.
- Correction d'un problème de désynchronisation entre les compteurs du tableau de bord administrateur et les panneaux de détails.
- Correction d'un problème de timezone dans les compteurs du tableau de bord administrateur.
- Correction d'un bug empêchant la bonne prise en compte des jours multi-employeurs dans les alertes réglementaires.
- Correction d'un problème de nested transaction lors de l'export des données CGU.
- Sanityzation du nom des deals Brevo pour éviter les erreurs.
