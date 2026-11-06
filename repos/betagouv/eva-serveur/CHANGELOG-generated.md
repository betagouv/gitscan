## Changelog : eva-serveur (30 derniers jours, au 05 novembre 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de la gestion des réponses et du suivi des bénéficiaires. L'introduction de l'option "Pas encore" permet désormais de planifier des relances automatiques, tandis que le nouveau système de "Statut de suivi" offre une meilleure visibilité sur l'accompagnement des utilisateurs. L'interface a également été enrichie de nouveaux outils de pilotage pour les administrateurs et de fonctionnalités d'exportation de documents (attestations).

### Évolutions fonctionnelles
- **Gestion des réponses et relances** :
    - Remplacement de l'option "Je ne sais pas" par "Pas encore", permettant de programmer une date de revue (7 jours, 14 jours, 1 mois ou date précise).
    - Amélioration de l'option "Autre" qui permet désormais d'ajouter une précision textuelle depuis la fiche d'évaluation, le tableau de bord ou la carte de suivi.
- **Suivi et pilotage** :
    - Mise en place d'un système de "Statut de suivi" permettant de trier et filtrer les listes de bénéficiaires et d'évaluations.
    - Ajout de boutons de consultation rapide ("Consulter X bénéficiaires/évaluations") sur les pages de campagne.
    - Affichage des actualités et des newsletters directement sur les tableaux de bord des comptes administratifs.
- **Documents et exports** :
    - Ajout de la génération et du téléchargement d'attestations de passation en format PDF.
    - Amélioration des exports (CSV/XLS) incluant désormais l'usage des structures.
- **Parcours et profils** :
    - Automatisation du calcul des profils de littératie et des restitutions en fonction des réponses et des abandons de parcours.
    - Affichage des sous-profils de littératie, même lorsqu'ils ne sont pas encore calculés.

### Évolutions techniques
- **Interface et composants (UI)** :
    - Mise à jour vers la version 1.15 du DSFR.
    - Création et refonte de nombreux composants réutilisables : Tags, Info-bulles, Boutons (variantes tertiaires et états désactivés), et composants spécifiques aux questions de mise en action.
    - Optimisation de l'expérience utilisateur : suppression de tags en arrière-plan sans rechargement de page.
- **Architecture et code** :
    - Refactoring important de la logique métier, notamment pour les modèles `MiseEnAction` et `StatutSuivi`.
    - Découpage du code JavaScript par écran pour une meilleure maintenabilité.
    - Consolidation des composants de tags en un composant unique.
- **Infrastructure et environnement** :
    - Mise à jour de Node.js (v22.23.4) et des dépendances Rails/JS.
    - Automatisation de la réinitialisation de la base de données de préproduction chaque vendredi.
- **Données** :
    - Enrichissement des données de test (intégration de nouveaux OPCO, SIRETs et scores QCM).
    - Passage des timestamps en précision `timestamp(6)`.

### Autres changements
- **Documentation** : Rédaction de nouvelles ADR (Architecture Decision Records) concernant le statut de suivi et la carte de suivi, et mise à jour de la documentation de développement (README, .env.template).
- **Nettoyage** : Suppression de fichiers Docker et de méthodes/styles obsolètes.
