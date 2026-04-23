## Changelog : anssi-portail (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du simulateur NIS2 avec l'ajout de nombreuses étapes et fonctionnalités, l'amélioration de la gestion des guides (ajout de documents, gestion des rôles), et l'implémentation d'une newsletter avec inscription et confirmation. Des corrections et optimisations diverses ont également été apportées à l'interface et à la sécurité.

### Évolutions fonctionnelles
- **Simulateur NIS2 :** Ajout de nombreuses étapes au simulateur (localisation, type de structure, activités, désignation OSE, etc.) et intégration de la logique de test d'éligibilité.
- **Gestion des guides :**
    - Possibilité d'ajouter des documents à un guide via une interface dédiée.
    - Gestion des rôles utilisateurs pour l'ajout de guides.
    - Copie du lien court d'un guide dans le presse-papier.
    - Amélioration de l'affichage et de la gestion des documents associés aux guides.
- **Newsletter :**
    - Implémentation d'un formulaire d'inscription à la newsletter.
    - Page de confirmation d'abonnement.
    - Intégration avec Brevo pour la gestion des abonnés.
- **Financements :** Le filtre "Toutes entités publiques" est maintenant placé en dernier dans la liste.
- **Partenaires :** Ajout des logos des nouveaux partenaires.
- **Réflexes Cyber :** Ajout de la ressource au catalogue.

### Évolutions techniques
- **Sentry :** Mise à jour de la version de Sentry et ajout de la configuration nécessaire pour son utilisation.
- **Dépendances :** Mises à jour de plusieurs dépendances (axios, yaml, picomatch, flatted, fast-xml-parser, zod, UI Kit) pour des raisons de sécurité et de performance.
- **Infrastructure :**
    - Utilisation de Svelte 5 pour le bouton SOIN.
    - Migration vers le bouton DSFR.
    - Amélioration de la gestion des assets pour les composants Svelte.
- **Code :**
    - Refactoring du code pour améliorer la lisibilité et la maintenabilité.
    - Utilisation de variables CSS pour une meilleure cohérence visuelle.
    - Suppression de code inutile.
    - Amélioration de la gestion des erreurs.
- **Tests :** Ajout de tests unitaires et d'intégration.
- **CI/CD :** Amélioration du pipeline CI/CD.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés.
- **SEO :** Ajout de meta descriptions et d'attributs alt pour améliorer le référencement.
- **Cellar :** Connexion du Cellar pour la gestion des guides.
- **Statistiques :** Mise à jour de la page des statistiques.
- **Correction de bugs :** Correction de divers bugs et améliorations de l'interface utilisateur.
- **Divers :** Amélioration de la gestion des images, des alertes et des messages d'information.
