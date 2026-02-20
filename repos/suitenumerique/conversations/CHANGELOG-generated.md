## Changelog : conversations (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec l'ajout d'un mode sombre persistant, une meilleure gestion des fichiers (notamment avec le support de S3 sans accès externe et un parseur PDF adaptatif), et des optimisations de performance, en particulier pour le rendu du markdown et l'entrée de texte dans le chat. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la compatibilité avec différents modèles d'IA.

### Évolutions fonctionnelles
- Ajout d'un mode sombre persistant, conservant le thème choisi par l'utilisateur. (#240)
- Amélioration de la gestion des fichiers avec la possibilité d'utiliser le stockage S3 sans accès externe. (#849)
- Implémentation d'un parseur PDF adaptatif pour une meilleure extraction du texte.
- Ajout de l'intégration FindRagBackend pour une recherche plus performante. (#209)
- Ajout d'un kit d'interface utilisateur avec support du mode sombre.
- Possibilité de supprimer des collections temporaires.
- Amélioration de l'intégration de l'API Find avec les sous-utilisateurs et les tags.
- Ajout d'un bouton de copie de code.
- Ajout d'un bouton de réessai.

### Évolutions techniques
- Migration vers `uv` pour améliorer les performances du backend.
- Optimisation du rendu du markdown en utilisant la division des blocs.
- Optimisation de la taille du bundle de surlignage de syntaxe.
- Mise à jour de Django.
- Mise à jour de Pydantic AI.
- Mise à jour de Next.js (version 5.3.9).
- Mise à jour de Protobuf (version 6.33.5).
- Correction de problèmes de keepalives lors du parsing de documents.
- Correction de tests.
- Vendorisation du fichier `mime.types` pour éviter les dépendances externes.

### Autres changements
- Mise à jour des chaînes de traduction. (#234)
- Correction de bugs liés aux formules mathématiques et aux traductions de la carrousel.
- Correction de l'affichage des documents PDF et standardisation de l'i18n.
- Suppression de code mort et de fichiers inutilisés.
- Suppression de la partie "pensée" de l'interface utilisateur.
- Désactivation de Trivy sur `yarn.lock` pour la génération de mails.
- Bump de la version à 0.0.13.
- Bump de la version à 0.0.12.
