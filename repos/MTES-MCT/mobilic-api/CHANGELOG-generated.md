## Changelog : mobilic-api (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, l'API Mobilic a bénéficié d'améliorations significatives en matière de sécurité, notamment avec l'ajout de l'authentification à deux facteurs (TOTP) et des fonctionnalités d'impersonation pour le support utilisateur. Des corrections et améliorations ont également été apportées à la gestion des exports de données, à l'interface d'administration et à la recherche de données NATINF.

### Évolutions fonctionnelles
- **Authentification :** Ajout de l'authentification à deux facteurs (TOTP) pour une sécurité renforcée.  Les utilisateurs peuvent désormais configurer et utiliser des codes TOTP pour se connecter [#685](https://github.com/MTES-MCT/mobilic-api/pulls/685).
- **Support Utilisateur :** Implémentation de fonctionnalités d'impersonation pour permettre aux administrateurs de support d'agir au nom d'un utilisateur, facilitant ainsi la résolution de problèmes [#685](https://github.com/MTES-MCT/mobilic-api/pulls/685).
- **Exports de données :** Correction d'un problème empêchant la mise à jour correcte de la date de transfert des données lors des exports CGU [#4d4cd00](https://github.com/MTES-MCT/mobilic-api/commit/4d4cd00).
- **Contrôles :** Ajout des articles dans les PDF BDC et intégration des NATINF personnalisés dans les exports [#72cb185](https://github.com/MTES-MCT/mobilic-api/commit/72cb185). Ajout de l'indicateur `isCTT` aux informations utilisateur pour les contrôles [#0162266](https://github.com/MTES-MCT/mobilic-api/commit/0162266).
- **Recherche NATINF :**  Ajout d'une fonctionnalité de recherche NATINF [#8fdb147](https://github.com/MTES-MCT/mobilic-api/pulls/700) et création/suppression de NATINF personnalisés via l'API [#b7f036c](https://github.com/MTES-MCT/mobilic-api/commit/b7f036c).
- **Page d'accueil Admin :** Refonte de la page d'accueil de l'interface d'administration pour une meilleure expérience utilisateur [#698](https://github.com/MTES-MCT/mobilic-api/pulls/698).
- **Rappels d'activation :** Implémentation d'emails de rappel pour l'activation des comptes utilisateurs [#697](https://github.com/MTES-MCT/mobilic-api/pulls/697).

### Évolutions techniques
- **Sécurité :** Ajout d'un audit pour l'impersonation, incluant la journalisation des actions et la restriction des cibles d'impersonation.
- **Refactoring :** Déduplication des requêtes pour les rappels d'activation afin d'améliorer les performances [#a7b2671](https://github.com/MTES-MCT/mobilic-api/commit/a7b2671).
- **Architecture :** Utilisation du claim `impersonate_as` dans les JWT pour l'impersonation, remplaçant l'ancien cookie `admin_token`.
- **Migrations :** Correction de l'ordre des révisions de migrations pour éviter des erreurs [#dd0f700](https://github.com/MTES-MCT/mobilic-api/commit/dd0f700), [#4997f34](https://github.com/MTES-MCT/mobilic-api/commit/4997f34).
- **Code :** Centralisation d'une fonction pour éviter la duplication dans le module de contrôle [#bb5e9cc](https://github.com/MTES-MCT/mobilic-api/commit/bb5e9cc).

### Autres changements
- **Documentation :** Ajout de support pour la création d'un super-administrateur dans le script de seed.
- **Tests :** Ajout de tests unitaires et d'intégration pour la sécurité (IDOR, etc.) et pour l'impersonation.
- **Corrections :** Correction d'un problème de désynchronisation du nom des deals Brevo.
