## Changelog : conversations (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois-ci, Conversations a franchi une étape importante avec une refonte technique de son interface pour offrir une navigation plus fluide et réactive. L'intelligence artificielle est devenue plus performante grâce à l'introduction de la synthèse automatique des échanges et à des instructions plus précises. L'expérience utilisateur a également été enrichie par de nouveaux indicateurs visuels, comme une barre de progression, et une gestion plus intuitive des documents.

### Évolutions fonctionnelles
- **Intelligence Artificielle** : introduction de la synthèse automatique des messages et optimisation des instructions (prompts) pour l'assistant DINUM afin d'améliorer la pertinence des réponses.
- **Interface & Expérience Utilisateur** : ajout d'une barre de progression lors des traitements, correction de l'affichage de l'icône "Docs" et amélioration du widget d'impact CO2.
- **Gestion documentaire** : optimisation de l'exportation des documents (gestion des titres et des extensions) et amélioration de la fluidité visuelle lors de la génération des premières réponses de l'IA.
- **Administration** : accélération et amélioration de l'affichage de la liste des conversations pour les administrateurs.
- **Paramètres** : déplacement des réglages d'analyse (analytics) vers la section générale pour une meilleure organisation.

### Évolutions techniques
- **Architecture & Frontend** : migration majeure de l'interface de Next.js vers Vite et React Router pour gagner en performance et en maintenabilité.
- **Intelligence Artificielle** : migration vers `pydantic-ai 2.x`, mise en place de la synthèse de messages en mode asynchrone et optimisation de la gestion de l'historique des messages.
- **Sécurité & Traitement de fichiers** : renforcement de la sécurité contre les fichiers PDF malveillants (bombes de décompression, fichiers trop volumineux) et migration de l'analyse de documents vers l'API Albert OCR.
- **Optimisation & Nettoyage** : suppression de plusieurs modules et outils de recherche web inutilisés (Tavily, Find RAG, Albert web search) et remplacement de la bibliothèque `requests` par `httpx` pour une gestion plus moderne des requêtes HTTP.
- **Backend** : optimisation de l'inscription des utilisateurs sur la liste de suivi Brevo.

### Autres changements
- Mise à jour des traductions (i18n).
