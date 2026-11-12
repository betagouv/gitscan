## Changelog : eva-serveur (30 derniers jours, au 10 novembre 2026)

### Résumé
Cette période a été marquée par l'amélioration significative du suivi des bénéficiaires, notamment avec l'introduction d'un statut « Pas encore » permettant de planifier des relances personnalisées. L'outil de gestion des évaluations (EVAPRO) a également été enrichi avec la génération d'attestations de passation et une meilleure visibilité des indicateurs de risque et de littératie.

### Évolutions fonctionnelles
- **Gestion du suivi et des relances** :
    - Introduction du statut « Pas encore » pour les mises en action, permettant de reporter une question à une date précise (7 jours, 14 jours, 1 mois ou date personnalisée).
    - Les actions reportées sont automatiquement masquées du tableau de bord jusqu'à leur date de revue.
    - Ajout de filtres, de tris et de colonnes dédiés au statut de suivi pour les listes de bénéficiaires et d'évaluations.
- **Amélioration des réponses** :
    - Possibilité de répondre « Autre » en apportant une précision textuelle (disponible sur la fiche, le tableau de bord et la carte de suivi).
    - Distinction claire entre une réponse « Pas encore » et une mise en action jamais répondue.
- **Évolutions EVAPRO** :
    - Affichage du taux de risque dans l'index dès qu'il est connu.
    - Génération et téléchargement d'attestations de passation au format PDF.
    - Calcul automatisé et affichage des sous-profils de littératie (ex: Production, Café de la place) en fonction des réponses ou des abandons.
- **Interface et navigation** :
    - Ajout de boutons de consultation rapide (« Consulter X bénéficiaires/évaluations ») sur les pages de campagne.
    - Amélioration de la visibilité des actualités et newsletters sur le tableau de bord.
    - Mise à jour de l'interface pour mieux respecter les maquettes et les standards DSFR (boutons, tags, info-bulles).

### Évolutions techniques
- **Infrastructure et dépendances** :
    - Montée de version de Node.js (v22.23.4), de Rails et du framework de design DSFR (v1.15).
    - Mise à jour des dépendances JavaScript et correction de la compatibilité avec JSON 3 et Ransack 6.
- **Tests et CI/CD** :
    - Optimisation du temps de démarrage des tests Jest en limitant les dossiers parcourus.
    - Intégration de l'exécution des tests Jest dans la CI et dans les tâches de validation.
- **Architecture et Refactoring** :
    - Unification et réécriture des composants d'interface (Tags, Boutons) pour une meilleure conformité au DSFR.
    - Refactorisation de la logique de « Mise en action » (déplacement de la logique dans le modèle, découpage du JavaScript par écran).
    - Standardisation du code de génération de PDF entre les restitutions et les attestations.
    - Centralisation de la logique de qualification et de détection des comptes sans évaluation.
- **Stabilité** :
    - Correction d'un risque de double soumission lors de la création de structures.

### Autres changements
- **Documentation** :
    - Ajout de plusieurs documents d'architecture (ADR 0001 et ADR 0002) concernant le statut de suivi et la carte de suivi.
    - Documentation des nouveaux états de mise en action et mise à jour du fichier `.env.template`.
- **Données de test** :
    - Mise à jour massive des données de test (OPCO, structures, comptes, évaluations) pour garantir la cohérence avec les environnements de production et de pré-production.
- **Nettoyage** :
    - Suppression de fichiers Docker inutilisés, de méthodes obsolètes et de styles CSS devenus superflus.
