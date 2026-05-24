## Changelog : drive (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec l'intégration de composants d'interface utilisateur plus modernes, l'ajout d'informations sur les droits d'utilisation et l'amélioration de la gestion des fichiers PDF. Des corrections de bugs et des optimisations ont également été apportées, notamment concernant la duplication d'éléments et la compatibilité des types de fichiers.

### Évolutions fonctionnelles
- Ajout d'un modal d'avertissement concernant les droits d'utilisation (entitlement disclaimer) [#101725](https://github.com/suitenumerique/drive/pull/101725)
- Amélioration du rendu des aperçus PDF avec affichage des pages et tests associés [#101725](https://github.com/suitenumerique/drive/pull/101725)
- Possibilité de configurer l'utilisation de PKCE pour l'authentification SSO [#101647](https://github.com/suitenumerique/drive/pull/101647)
- Ajout d'événements de suivi (PostHog) pour le changement de type de colonne et la duplication d'éléments.
- Ajout de métriques d'organisation à l'API d'utilisation.
- Possibilité d'accepter le type MIME CDFV2 pour une meilleure compatibilité avec les fichiers détectés par libmagic.

### Évolutions techniques
- Remplacement de l'ID de version par l'ETag pour la compatibilité WOPI.
- Refactorisation des composants d'icônes de fichiers et d'aperçus vers la bibliothèque d'interface utilisateur (ui-kit).
- Refactorisation de la gestion des droits (entitlements) dans un package backend dédié.
- Amélioration de la gestion des transactions lors de la duplication d'éléments.
- Modification de la signature de la fonction `compute` dans le backend de stockage pour accepter un queryset.
- Mise à jour de la bibliothèque Django en version 5.2.14 (correction de sécurité).
- Mise à jour de la bibliothèque urllib3 en version 2.7.0 (correction de sécurité).
- Mise à jour de la version de la bibliothèque ui-kit.

### Autres changements
- Mise à jour de la documentation (changelog).
- Ajout de logs pour la taille maximale de fichier attendue par WOPI.
- Ajout de tests E2E pour les avertissements relatifs aux droits d'utilisation et les aperçus PDF.
- Suppression de la fonctionnalité de mirroring.
- Mise à jour des dépendances Python.
