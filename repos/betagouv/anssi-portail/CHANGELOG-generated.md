## Changelog : anssi-portail (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la performance via le rendu côté serveur (SSR) de nombreuses pages, la modernisation de l'interface utilisateur avec l'adoption de nouveaux composants DSFR et une refonte de l'expérience utilisateur du parcours de sécurisation. Des corrections de sécurité et des améliorations de la CI/CD ont également été apportées.

### Évolutions fonctionnelles
- **Parcours de sécurisation :** Amélioration significative de l'expérience utilisateur avec l'ajout de la gestion des modules, de la progression, des badges de complétion et de la persistance du parcours de l'utilisateur.
- **Téléchargement des récompenses :** Préparation de la création d'archives ZIP contenant les récompenses du parcours sécurisation. [#94d7769](https://github.com/betagouv/anssi-portail/issues/94d7769)
- **Page NIS2 :** Amélioration de l'affichage et de la navigation sur la page NIS2.
- **Guides :** Amélioration de l'affichage des guides et intégration dans le catalogue.
- **Affichage des mesures :** Amélioration de l'affichage des mesures dans le parcours de sécurisation, avec la possibilité de les exporter en CSV.
- **Modales de tutoriel :** Ajout de modales de tutoriel pour guider l'utilisateur.
- **Suivi Pixel :** Implémentation du suivi des données avec consentement utilisateur.

### Évolutions techniques
- **Rendu côté serveur (SSR) :** Implémentation du rendu côté serveur pour de nombreuses pages (accueil, associations, financements, sessions de groupe, guides, collectivités, NIS2, etc.) afin d'améliorer la performance et le SEO.
- **Composants DSFR :** Migration vers des composants DSFR (Design System de la République Française) pour une meilleure cohérence visuelle et accessibilité.
- **Refactoring :** Refactoring de plusieurs composants pour améliorer la maintenabilité et la lisibilité du code.
- **CI/CD :** Améliorations de la configuration CI/CD, notamment l'ajout d'étapes de scan antivirus et la sécurisation des secrets.
- **Dépendances :** Mise à jour de plusieurs dépendances, incluant des correctifs de sécurité.
- **Nix Shell :** Ajout d'un Nix Shell pour faciliter le développement en local.
- **Tests :** Ajout de tests de snapshot pour les bannières.

### Autres changements
- **Documentation :** Mise à jour de la documentation et du README.
- **Configuration :** Amélioration de la configuration des secrets et des variables d'environnement.
- **Nettoyage de code :** Suppression de code inutile et amélioration de la structure du code.
- **SEO :** Amélioration du SEO avec la redirection de l'ancienne page /guides vers /catalogue.
- **Matomo :** Ajout de la campagne Matomo à l'origine des demandes d'aide.
