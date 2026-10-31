## Changelog : ComparIA (30 derniers jours, au 28 octobre 2026)

### Résumé
Ce mois-ci, ComparIA a connu une montée en puissance de ses capacités d'administration et de sa sécurité. L'introduction de la modération automatique par IA et d'un nouveau tableau de bord d'activité permet une gestion plus fine de la plateforme. Parallèlement, des mesures importantes ont été prises pour protéger les données sensibles (chiffrement des clés) et renforcer la lutte contre les abus et le spam, tout en améliorant l'expérience utilisateur sur mobile et les traductions.

### Évolutions fonctionnelles
- **Modération par IA** : Introduction des "Prompt Checks" permettant d'utiliser des modèles de décision pour analyser et filtrer les messages selon des critères prédéfinis [#830](https://github.com/betagouv/ComparIA/pull/830).
- **Administration enrichie** : 
    - Ajout d'un panneau d'activité pour suivre les statistiques et les événements de la plateforme.
    - Possibilité de configurer les seuils du classement (leaderboard) directement depuis l'interface.
    - Gestion simplifiée des critères de modération et visualisation des messages refusés ou signalés.
- **Contrôle des modèles** : Possibilité de verrouiller certains modèles pour qu'ils ne soient plus disponibles en mode de sélection personnalisé [#827](https://github.com/betagouv/ComparIA/pull/827).
- **Export et données** : Ajout d'un bouton pour télécharger les données de classement et publication des fichiers `models.json` avec les jeux de données.
- **Expérience utilisateur** : 
    - Amélioration de l'affichage sur mobile (reflow de l'arène).
    - Corrections de focus et de navigation après un vote.
    - Enrichissement des traductions, notamment pour le danois.
- **Confidentialité** : Intégration de la gestion du refus de suivi Matomo sur la page de confidentialité.

### Évolutions techniques
- **Sécurité et lutte contre les abus** : Renforcement massif de la protection contre le spam et les comportements malveillants (limitation par IP et par IPv6, gestion des budgets de caractères, captchas dynamiques et détection de répétition de prompts) [#791](https://github.com/betagouv/ComparIA/pull/791).
- **Protection des données sensibles** : Mise en place du chiffrement des secrets stockés (clés API, identifiants de publication) et d'un mécanisme de rotation des clés [#701](https://github.com/betagouv/ComparIA/pull/701).
- **Gestion du cycle de vie des données** : Automatisation de la purge des comptes inactifs et des données obsolètes (données personnelles, cohortes) via des tâches planifiées (CronJobs).
- **Authentification** : Amélioration de la robustesse du protocole OIDC (sécurisation des callbacks, validation des jetons, gestion des logos d'authentification) [#763](https://github.com/betagouv/ComparIA/pull/763).
- **Optimisation** : Amélioration des performances de la base de données (indexation) et déchargement de certaines tâches lourdes (comptage de tokens) du thread principal.

### Autres changements
- **Documentation** : Mise à jour complète de la documentation d'administration (modération, gestion des secrets, purge des données, suivi d'activité).
- **CI/CD** : Suppression du job CodeQL du workflow de sécurité.
