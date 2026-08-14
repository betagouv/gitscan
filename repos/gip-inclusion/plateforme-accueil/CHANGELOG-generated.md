## Changelog : plateforme-accueil (30 derniers jours, au 10 août 2026)

### Résumé
Le projet a franchi une étape majeure avec la refonte complète de la page d'accueil et la transition vers une architecture Django robuste. L'accent a été mis sur une intégration fluide et sécurisée via iframe, ainsi que sur la mise en place d'une infrastructure de déploiement automatisée pour garantir la stabilité de la plateforme.

### Évolutions fonctionnelles
- **Refonte de la page d'accueil** : Mise en place de la nouvelle maquette visuelle pour la landing page. [#3](https://github.com/gip-inclusion/plateforme-accueil/pull/3)
- **Aperçu intégré** : Ajout d'un exemple de rendu de la maquette directement sur la page d'accueil pour faciliter la visualisation.

### Évolutions techniques
- **Architecture & Framework** : 
    - Migration d'un bundle HTML unique vers une structure Django complète (templates, fichiers statiques et gestion des assets).
    - Extraction d'un template de base pour uniformiser le rendu de toutes les pages.
- **Optimisation de l'intégration (Iframe)** :
    - Amélioration du système de redimensionnement automatique pour assurer un affichage fluide du contenu sans décalage de la vue.
    - Intégration d'un script côté hôte pour faciliter l'inclusion de la plateforme.
    - Optimisation de la gestion des icônes (SVG inline) pour garantir leur affichage dans des environnements d'iframe sécurisés (sandboxed).
- **Sécurité & Analytics** :
    - Mise en place d'une politique de sécurité (CSP) adaptée à l'intégration en iframe, configurable via variable d'environnement.
    - Intégration du gestionnaire de balises Matomo pour le suivi de l'audience.
- **Infrastructure & DevOps** :
    - Mise en place de la conteneurisation avec Docker et automatisation des tâches via un Makefile.
    - Configuration des workflows de CI/CD (GitHub Actions) pour les tests et le déploiement.

### Autres changements
- **Documentation** : Initialisation de la documentation du projet (README, CLAUDE.md).
- **Standardisation** : Passage des commentaires de code en anglais et nettoyage des fichiers de notes locaux.
