## Changelog : eva-serveur (30 derniers jours, au 13 novembre 2026)

### Résumé
Cette période est marquée par une amélioration majeure du suivi des bénéficiaires. L'introduction de l'option "Pas encore" permet de mieux gérer les relances en planifiant des dates de revue, offrant ainsi une gestion plus fine des accompagnements. Le tableau de bord et les listes ont été enrichis de nouveaux indicateurs (statut de suivi, taux de risque) et de filtres pour faciliter le pilotage. Enfin, de nouveaux outils administratifs, comme la génération d'attestations de passation en PDF, ont été déployés.

### Évolutions fonctionnelles
- **Gestion du suivi et des relances** :
    - Introduction de l'option "Pas encore" pour les mises en action, permettant de reporter une réponse et de programmer une date de revue (7 jours, 14 jours, 1 mois ou date précise) [#EVA-1186](https://github.com/betagouv/eva-serveur/issues/1186).
    - Distinction claire entre une réponse "Pas encore" et une mise en action jamais répondue.
    - Ajout de l'option "Autre" avec un champ de précision pour enrichir les réponses sur la fiche évaluation, le tableau de bord et la carte de suivi.
- **Visibilité et pilotage** :
    - Ajout d'une colonne et de filtres "Suivi" dans les listes de bénéficiaires et d'évaluations.
    - Affichage du taux de risque directement dans l'index EVAPRO dès qu'il est connu.
    - Ajout de boutons de consultation rapide ("Consulter X bénéficiaires/évaluations") sur les pages de campagne.
- **Outils administratifs** :
    - Possibilité pour les administrateurs de consulter et modifier l'OPCO d'une structure locale.
    - Mise à disposition d'un bouton de téléchargement pour l'attestation de passation (format PDF) sur les restitutions EVAPRO.
    - Affichage des actualités du tableau de bord pour les comptes administratifs.
- **Interface utilisateur (UI)** :
    - Refonte de l'interface de mise en action sur le tableau de bord pour une utilisation plus fluide (une action à la fois) [#EVA-1156](https://github.com/betagouv/eva-serveur/issues/1156).
    - Amélioration de l'ergonomie et de l'alignement des composants selon les maquettes (DSFR) [#EVA-1209](https://github.com/betagouv/eva-serveur/issues/1209).

### Évolutions techniques
- **Architecture et Code** :
    - Refactorisation importante de la logique de suivi et des composants UI (fusion de composants Tag, réécriture des composants de mise en action et de réponse).
    - Optimisation de la gestion des fichiers via Active Storage (levée de la limite de préchargement par IP).
    - Centralisation de la logique métier (statuts de suivi, qualifications) dans les modèles Ruby.
    - Uniformisation de la génération de PDF entre les restitutions et les attestations.
- **Performance et CI/CD** :
    - Optimisation du temps d'exécution des tests Jest en limitant le périmètre de recherche et en les intégrant à la CI.
    - Mise à jour de l'environnement de développement (passage à Node.js 22).
- **Données et Schéma** :
    - Automatisation de la régénération du schéma de base de données (ERD) après chaque migration.
    - Mise à jour des questions du questionnaire Numératie 2024 et alignement des données de test (OPCO, structures) sur la production.

### Autres changements
- **Documentation** :
    - Rédaction de nouvelles architectures de décision (ADR 0001 sur le statut de suivi et ADR 0002 sur la carte de suivi).
    - Documentation des variables d'environnement (`.env.template`) pour S3 et les paramètres de mise en action.
- **Maintenance** :
    - Nettoyage du projet : suppression de la variable `ACTIVE_EVAPRO`, du Dockerfile inutilisé et de certains styles obsolètes.
    - Renommage du fichier `CLAUDE.md` en `AGENTS.md`.
