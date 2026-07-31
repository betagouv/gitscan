## Changelog : anssi-portail (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur avec l'implémentation d'une nouvelle identité visuelle, l'optimisation du parcours de sécurisation et l'amélioration des performances grâce au rendu côté serveur (SSR) pour plusieurs pages du site. Des corrections et des mises à jour de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Mise à jour de l'identité visuelle (DA) sur de nombreuses pages, incluant l'accueil, les pages de services, les guides, les financements, les contacts, les niveaux de maturité et les associations.
- Implémentation d'un nouveau héros (bannière) sur plusieurs pages pour une meilleure présentation visuelle.
- Amélioration du parcours de sécurisation :
    - Affichage des mesures sous forme de liste.
    - Gestion de la prise en compte des mesures.
    - Ajout de badges de progression et d'informations sur l'état d'avancement des modules.
    - Possibilité de naviguer vers les modules.
    - Affichage des interlocuteurs associés aux mesures.
- Ajout d'un système de consentement pour le suivi via Pixel.
- Mise à jour du badge cyberdépart dans l'encart associé.
- Correction de l'affichage du titre de page et de la carte d'une mesure.
- Correction de la redirection vers la page accédée avant authentification.
- Correction de l'affichage du fil d'Ariane.
- Mise à jour des liens et des descriptions sur certaines pages.

### Évolutions techniques
- Implémentation du rendu côté serveur (SSR) pour de nombreuses pages, améliorant ainsi les performances et le SEO :
    - Pages des associations, collectivités, financements, guides, NIS2, contacts.
    - Composants tels que les liens, les cartes, les filtres, les WebC.
- Refonte de l'architecture pour faciliter l'intégration du SSR.
- Utilisation de Svelte 5 pour certains composants.
- Amélioration de la gestion des dépendances et des versions.
- Ajout de tests unitaires et d'intégration.
- Mise à jour des outils de CI/CD pour inclure des scans antivirus.
- Amélioration de la configuration et de la gestion des secrets.
- Ajout d'un Nix Shell pour le développement en local.
- Migration vers des UUID v7 pour la génération de clés primaires.

### Autres changements
- Mise à jour de la documentation.
- Correction de l'indentation des fichiers YAML de déploiement.
- Ajout de métadonnées Open Graph et Twitter pour améliorer le partage sur les réseaux sociaux.
- Suppression de code inutile et nettoyage du codebase.
- Correction de bugs mineurs et améliorations de la stabilité.
- Ajout du skill d'agent Playwright.
- Mise à jour des dépendances (hors mises à jour automatiques).
- Correction de la navigation tertiaire.
- Ajout de la campagne Matomo à l'origine des demandes d'aide.
- Suppression d'un test qui ne pouvait plus fonctionner.
