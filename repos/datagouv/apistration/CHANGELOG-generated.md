## Changelog : apistration (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, la documentation et l'expérience utilisateur, notamment avec l'intégration de Simplifions et des améliorations de la gestion des accès et des scopes des API. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- **Sécurité :** Correction d'une vulnérabilité de type tabnapping sur les liens DataPass ciblant `_blank` [#240](https://github.com/datagouv/apistration/pull/240). Correction d'une vulnérabilité XSS dans le lien `external_id` de DataPass [#240](https://github.com/datagouv/apistration/pull/240).
- **Authentification :** Redirection vers la page demandée après la connexion [#238](https://github.com/datagouv/apistration/pull/238).
- **Simplifions :** Refonte de l'intégration de Simplifions, incluant la gestion des fiches pratiques et des cas d'usage, avec amélioration des performances et de la structure des données.  Remplacement de la FAQ API Entreprise par un lien vers la page Simplifions.
- **API Particulier :**  Ajout de la documentation et des scopes pour les API Particulier, avec affichage des scopes sur les fiches d'API et dans les réponses.
- **Admin :** Ajout d'un suivi des activités des administrateurs pour l'audit et la sécurité.  Amélioration de la gestion des éditeurs dans l'interface d'administration.
- **DGFIP TVA :** Ajout d'un endpoint DGFIP TVA avec des informations sur la nouveauté et la gestion des erreurs.

### Évolutions techniques
- **Infrastructure :** Mise à jour des dépendances Ruby, Rails, et des actions GitHub.
- **Tests :** Amélioration de la robustesse des tests, notamment pour l'API DGFIP TVA.
- **Refactoring :** Refactorisation du code Simplifions pour une meilleure performance et maintenabilité.
- **CI/CD :**  Correction de problèmes de CI liés à l'API DGFIP TVA.
- **Documentation :** Amélioration de la documentation, notamment pour l'intégration FranceConnect et les scopes des API.
- **Sécurité :** Renforcement de la sécurité des sessions avec une expiration après 12h d'inactivité et une protection anti-fixation.
- **Pings :** Amélioration de la gestion des pings et correction des URLs cassées.

### Autres changements
- Correction de typos et amélioration de la qualité du code.
- Ajout de tests pour la nouvelle fonctionnalité d'audit des activités d'administration.
- Mise à jour du changelog pour refléter les nouvelles fonctionnalités et corrections.
- Ajout de datasets de test pour CNous.
- Suppression de code inutile et amélioration de la lisibilité du code.
- Ajout d'un filtre de statut pour les habilitations des fournisseurs dans le tableau de bord.
- Affichage de l'ID interne de l'utilisateur sur la page de compte.
- Ajout d'une skill Hyperping pour les incidents.
- Correction de problèmes de cache pour l'API TVA tabulaire.
- Amélioration de la gestion des erreurs pour l'API DJEPVA.
- Ajout de la possibilité de filtrer les incidents dans le tableau de bord des fournisseurs.
