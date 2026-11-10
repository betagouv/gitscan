## Changelog : gestion-eclairee (30 derniers jours, au 08 novembre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante dans l'automatisation de l'analyse de données. L'une des évolutions majeures est l'amélioration de la capacité à traiter les factures non dématérialisées (PDF) grâce à de nouveaux outils d'extraction. Parallèlement, l'intégration de capacités d'intelligence artificielle via le protocole MCP permet désormais de mieux guider les agents conversationnels dans l'analyse des données budgétaires. L'ensemble du pipeline de traitement de données a été optimisé pour être plus rapide et plus stable.

### Évolutions fonctionnelles
- **Amélioration de l'extraction de documents** : Intégration de la technologie PDF4LLM pour structurer et extraire les données des factures au format PDF non dématérialisées.
- **Meilleure visibilité sur les processus** : Ajout de statistiques détaillées sur l'extraction PDF dans la synthèse BUDAT et affichage des totaux réels dans les barres de progression de classification.
- **Fiabilisation de la synchronisation** : Amélioration de la détection des lignes manquantes lors des exports BUDAT/AUGDT et gestion plus précise des montants par référence facture.
- **Suivi de l'activité** : Ajout de rapports sur les factures restant à traiter par fournisseur.

### Évolutions techniques
- **Intelligence Artificielle & MCP** : 
    - Mise en place d'un serveur MCP (Model Context Protocol) pour assister les agents LLM.
    - Exposition de métadonnées budgétaires en lecture seule pour les agents.
    - Implémentation du support OAuth2 pour le protocole MCP et ajout d'outils de vérification de connectivité.
- **Optimisation du pipeline de données** :
    - Parallélisation de l'extraction PDF et gestion de la mémoire (RAM) par lots pour éviter les saturations.
    - Intégration de l'extraction PDF directement dans le cycle de vie des données (pipeline bronze/silver/gold).
    - Traitement par lots (batching) pour les fichiers XML et Factur-X et pagination de la construction des données de facturation.
    - Refactoring du modèle `Facture` vers des schémas Pydantic pour une meilleure validation des données.
- **Stabilité et Performance** :
    - Correction de bugs liés à la navigation automatisée (Playwright) et à la gestion des téléchargements.
    - Optimisation des processus de classification par lots streamés.

### Autres changements
- **Documentation** : Ajout de guides pour le protocole de test local du serveur MCP et les procédures de lancement.
- **Configuration** : Mise à jour des fichiers de dépendances et du Procfile pour supporter le nouveau serveur MCP.
