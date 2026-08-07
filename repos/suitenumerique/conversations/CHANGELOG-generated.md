## Changelog : conversations (30 derniers jours, au 06/08/2026)

### Résumé
Ce mois-ci, Conversations a franchi une étape importante dans l'amélioration de l'expérience utilisateur grâce à l'introduction de la synthèse automatique des messages et d'une meilleure gestion des documents. Le projet a également renforcé sa sécurité et ses performances grâce à l'adoption de traitements asynchrones et de nouvelles protections contre les fichiers malveillants.

### Évolutions fonctionnelles
- **Synthèse de conversation** : Ajout de la capacité de résumer les messages, accompagnée d'une barre de progression pour le suivi de l'opération.
- **Gestion des documents** : 
    - Nouvelle fonctionnalité "Modifier dans Docs" pour faciliter l'édition des messages exportés.
    - Amélioration de l'export de documents avec des titres localisés et une meilleure gestion des extensions Markdown.
- **Expérience utilisateur (UX)** :
    - Amélioration de la fluidité visuelle lors de l'affichage de la première réponse de l'IA.
    - Correction de l'affichage des titres de conversation dans le panneau latéral réduit.
    - Amélioration du widget d'impact CO2 (corrections et ajout d'infobulles sur les messages de l'assistant).

### Évolutions techniques
- **Performance et Asynchronisme** :
    - Passage en mode asynchrone pour la synthèse des messages et le traitement des fichiers de conversation.
    - Accélération de l'affichage de la liste des conversations dans l'interface d'administration.
- **Sécurité** :
    - Renforcement de la protection lors du parsing de fichiers (protection contre les bombes de décompression et les PDF de taille excessive).
- **Architecture et Refactoring** :
    - Migration du parsing PDF vers l'API Albert OCR et suppression des anciens modules de recherche obsolètes.
    - Refactorisation de composants frontend (notamment la bannière de saisie) pour une meilleure réutilisabilité.
    - Optimisation de la gestion de l'historique pour éviter les synthèses redondantes.
- **Corrections techniques** :
    - Alignement des requêtes RAG avec les contrats d'API actuels.
    - Optimisation de l'inscription des utilisateurs à la liste de suivi Brevo.

### Autres changements
- **Internationalisation** : Mise à jour des chaînes de caractères traduites.
- **Tests** : Nettoyage et simplification de la configuration de l'environnement de tests et des fixtures.
