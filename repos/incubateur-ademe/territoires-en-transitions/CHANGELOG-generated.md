## Changelog : territoires-en-transitions (30 derniers jours, au 31 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape majeure avec le déploiement de l'outil "Aide à la priorisation" et une refonte profonde de l'importation de plans par intelligence artificielle. L'expérience utilisateur a été considérablement enrichie par une meilleure gestion des indicateurs, une automatisation accrue des processus de suivi PCAET et une interface plus intuitive grâce à l'ajout de visites guidées.

### Évolutions fonctionnelles
- **Aide à la priorisation** : 
    - Lancement de l'outil avec une nouvelle interface incluant une matrice interactive (impact vs mobilisation), un treemap et un classement des leviers.
    - Ajout d'une visite guidée pour accompagner les utilisateurs dans la découverte de l'outil.
    - Possibilité de sauvegarder des actions directement depuis le volet de priorisation.
- **Importation assistée par IA** : 
    - Amélioration massive de la robustesse de l'import (support des formats Word, PDF, Excel, CSV).
    - Capacité de reprise automatique des imports interrompus ou en échec.
    - Meilleure précision de la structuration des données (détection des secteurs réglementaires, des partenaires et des financements).
- **Indicateurs et suivi** : 
    - Introduction de nouvelles périodicités de saisie (mensuelle, trimestrielle, semestrielle).
    - Possibilité d'exporter les indicateurs directement en format Excel.
    - Harmonisation de l'interface de saisie des résultats et des objectifs.
- **Gestion des plans et démarches (PCAET)** : 
    - Automatisation de l'archivage des anciens plans lors de l'adoption d'un nouveau PCAET.
    - Amélioration du suivi des dossiers d'instruction et distinction entre les EPCI obligés et volontaires.
    - Gestion optimisée des secteurs réglementaires au sein des fiches d'actions.
- **Référentiels** : 
    - Nouvelle vue détaillée pour les actions de référence.
    - Export des scores enrichi avec des colonnes thématiques, d'adaptation et de labellisation.

### É évolutions techniques
- **Intelligence Artificielle** : 
    - Diversification des modèles utilisés (intégration de Mistral AI et Gemini) et optimisation de l'orchestration des appels (parallélisation des tâches d'extraction et gestion fine des quotas).
- **Observabilité et Monitoring** : 
    - Migration du suivi des erreurs de Sentry vers PostHog.
    - Intégration d'OpenTelemetry pour la gestion des traces et des logs.
- **Architecture et Performance** : 
    - Migration vers Strapi 5.
    - Remplacement progressif de PostgREST par tRPC pour une meilleure gestion des données et de la sécurité.
    - Optimisation des processus de calcul des scores et de la synchronisation des données.
- **Infrastructure et Sécurité** : 
    - Renforcement de la sécurité des connexions à la base de données PostgreSQL via la vérification TLS.
    - Mise à jour des environnements de CI/CD (Node.js, Playwright) et optimisation des builds d'images Docker.

### Autres changements
- **Documentation** : Mise à jour des documents d'architecture (ADR) et des guides de transition.
- **Site vitrine** : Refonte de la présentation du service PCAET et de la FAQ pour une meilleure clarté auprès du public.
