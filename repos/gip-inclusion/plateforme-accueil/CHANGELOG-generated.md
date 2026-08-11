## Changelog : plateforme-accueil (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois a été marqué par la structuration initiale et la refonte majeure de la plateforme. Le projet est désormais pleinement opérationnel avec une nouvelle page d'accueil et une infrastructure technique robuste, optimisée spécifiquement pour une intégration fluide et sécurisée via iframe.

### Évolutions fonctionnelles
- **Refonte de la page d'accueil** : Refonte complète de la landing page pour améliorer l'expérience utilisateur [#3](https://github.com/gip-inclusion/plateforme-accueil/pull/3).
- **Amélioration de la présentation** : Affichage direct de la maquette d'exemple pour faciliter la visualisation du rendu final.

### Évolutions techniques
- **Infrastructure et CI/CD** : Mise en place complète de l'environnement de développement et de déploiement (Docker, Makefile, workflows GitHub Actions pour la CI et le déploiement).
- **Optimisation de l'intégration (iframe)** : 
    - Amélioration de la gestion du redimensionnement automatique pour éviter les problèmes d'affichage lors du chargement du contenu.
    - Optimisation de la compatibilité des icônes (SVG inline) pour garantir leur affichage dans des environnements sécurisés (sandboxed iframes).
    - Ajout de la possibilité de configurer les politiques de sécurité (CSP) via des variables d'environnement.
- **Architecture logicielle** : 
    - Transition d'un bundle HTML unique vers une architecture Django standard (utilisation de templates et de fichiers statiques).
    - Création d'un template de base pour uniformiser l'ensemble des pages.
- **Analytique** : Intégration du gestionnaire de balises Matomo pour le suivi de l'audience.

### Autres changements
- **Documentation** : Ajout du fichier README et de règles de développement (CLAUDE.md).
- **Standardisation** : Passage des commentaires de code en anglais pour assurer la cohérence avec les standards du projet.
