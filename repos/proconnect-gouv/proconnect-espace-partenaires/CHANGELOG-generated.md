## Changelog : proconnect-espace-partenaires (30 derniers jours, au 05 août 2026)

### Résumé
Ce mois-ci, l'Espace Partenaires s'est concentré sur la transition vers ProConnect et le renforcement de la conformité. Les partenaires bénéficient de nouvelles capacités de gestion (comme la suppression d'application), d'une interface utilisateur améliorée et de nouveaux outils de suivi de conformité (MFA), tout en simplifiant les méthodes d'authentification pour plus de clarté.

### Évolutions fonctionnelles
- **Gestion et Sécurité**
  - Ajout de la possibilité pour les partenaires de supprimer leur propre application [#416](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/416).
  - Simplification de l'authentification avec la suppression de la connexion par code OTP par email et documentation de la procédure de récupération de compte [#430](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/430).
  - Correction d'un bug empêchant un utilisateur de tenter de se supprimer lui-même [#403](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/403).
  - Annulation de la fonctionnalité d'ajout de collaborateur (revert) [#393](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/393).
- **Conformité et Information**
  - Mise en place de checklists de conformité MFA pour les FI [#425](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/425).
  - Communication renforcée sur la migration vers ProConnect via des bannières et des annonces dédiées dans le portail [#408](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/408).
- **Expérience Utilisateur (UI/UX)**
  - Améliorations générales de l'interface et de la clarté des messages d'information [#413](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/413), [#23d22ca](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/417) et [#a9909a3](https://github.com/proconnect-gouv/proconnect-espace-partenaires/commit/a9909a3).
  - Ajout d'un bouton d'accès direct à ProConnect dans l'Espace Partenaires [#361](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/361).

### Évolutions techniques
- **Infrastructure et API**
  - Migration vers la nouvelle image `api-partenaires` pour l'environnement Docker Compose [#28d48de](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/418) et [#3565b0a](https://github.com/proconnect-gouv/proconnect-espace-partenaires/commit/3565b0a).
- **CI/CD et Tests**
  - Optimisation des pipelines CI avec une meilleure gestion du cache des dépendances [#427](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/427).
  - Amélioration de la fiabilité des tests en réduisant leur dépendance au sandbox ProConnect [#2febfa6](https://github.com/proconnect-gouv/proconnect-espace-partenaires/commit/2febfa6).
  - Validation de la compatibilité de la commande `npm prune` dans le cycle de CI [#407](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/407).
- **Maintenance**
  - Résolution de conflits de dépendances concernant le module `nodemailer` [#409](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/409).

### Autres changements
- **Documentation**
  - Mise à jour des liens vers le portail partenaire en HTTPS [#432](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/432).
  - Ajout de schémas explicatifs sur le fonctionnement de ProConnect [#400](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/400).
  - Diverses corrections de coquilles et améliorations de la documentation de conformité.
- **Qualité du code**
  - Uniformisation du style de code via l'application de Prettier sur l'ensemble du projet [#402](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/402).
