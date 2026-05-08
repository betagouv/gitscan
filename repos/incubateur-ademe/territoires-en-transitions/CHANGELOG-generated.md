## Changelog : territoires-en-transitions (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des données, la stabilisation de l'infrastructure et l'expérience utilisateur, notamment au niveau des fiches action, des plans et des rapports. Des efforts importants ont été réalisés pour optimiser les performances et la fiabilité de la plateforme, avec une migration vers tRPC pour certaines opérations et une refonte de la gestion des backups.

### Évolutions fonctionnelles
- **Fiches Action :**
    - Ajout de la possibilité d'ajouter des documents à une fiche action via un nouveau point trpc.
    - Amélioration de l'édition des fiches action avec une nouvelle interface et des composants plus performants.
    - Possibilité pour les contributeurs pilotes de créer, modifier et supprimer des sous-actions.
    - Gestion fine des sous-types de collectivités pour l'arrivée du nouveau référentiel.
- **Plans :**
    - Amélioration de la gestion de la complétion des plans, avec suppression des parties frontales obsolètes.
    - Possibilité de créer un plan depuis un panier d'actions via un nouvel endpoint backend.
    - Correction du lien vers la racine du plan dans le fil d'Ariane.
- **Rapports :**
    - Ajout de la possibilité d'inclure la dernière note dans les rapports.
    - Tri des fiches dans les rapports.
    - Amélioration de la génération des rapports pour éviter certaines requêtes et limiter la parallélisation.
- **Indicateurs :**
    - Amélioration de la recherche de collectivités.
    - Préservation des favoris et de la confidentialité lors de la mise à jour partielle d'un indicateur.
- **Autres :**
    - Amélioration de la synchronisation Calendly Airtable.
    - Modification pour remplacer les statistiques d'usage par des statistiques d'impacts et de résultats.
    - Correction de la pagination de la page Actualités.

### Évolutions techniques
- **Architecture & Backend :**
    - Migration de certaines opérations de la fiche action de Supabase vers tRPC pour améliorer les performances et la flexibilité.
    - Utilisation de transactions pour sauvegarder l'historique des statuts et commentaires des actions.
    - Refactor de l'historisation des mises à jour des Fiches d'Action pour utiliser le backend.
    - Suppression de certains endpoints tRPC dans l'application panier.
- **Infrastructure & CI/CD :**
    - Mise en place d'une stratégie de backup et de restore de la base de données.
    - Ajout de scripts de backup et restore dans le CI/CD.
    - Mise à jour de l'adresse d'envoi d'email.
    - Ajout du dashboard privé Streamlit dans le healthcheck.
    - Reset des passwords lors de la restauration de la base de données en staging.
- **Optimisations :**
    - Ajout d'index sur les tables d'historique pour améliorer les performances des requêtes.
    - Ajout d'un debounce sur les RichTextEditor pour alléger les appels au serveur de la FA.
    - Suppression de code obsolète et simplification de certaines parties du code.
    - Amélioration de l'isolation des tests et parallélisation des tests.

### Autres changements
- Mise à jour du texte de description des rôles des membres.
- Suppression de certaines vues et fonctions sur les questions/réponses/thématiques de personnalisation.
- Amélioration de l'ergonomie de l'EDL avec l'utilisation du sidepanel.
- Mise à jour des templates d'import de plan.
- Correction de typos et amélioration de la lisibilité du code.
- Ajout de tests unitaires et d'intégration.
- Suppression de feature flags inutiles.
- Ajout de configuration pour Claude.
- Amélioration de la gestion des erreurs et des logs.
- Mise à jour des dépendances.
