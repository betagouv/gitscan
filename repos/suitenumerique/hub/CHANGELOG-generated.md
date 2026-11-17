## Changelog : hub (30 derniers jours, au 11 novembre 2026)

### Résumé
Cette période est marquée par le passage en version 0.1.0. Les développements se sont concentrés sur l'amélioration de l'expérience de messagerie (interface plus fluide, gestion des notifications et des fils de discussion), l'optimisation des performances de chargement et la mise en place d'outils d'analyse pour mieux comprendre l'utilisation de la plateforme.

### Évolutions fonctionnelles
- **Messagerie et interactions** :
    - Support du formatage Markdown pour les messages.
    - Possibilité de mentionner des utilisateurs directement depuis le champ de saisie.
    - Affichage détaillé des réactions (visualisation de qui a réagi au survol).
    - Gestion des brouillons par conversation et par fil de discussion pour éviter les pertes de saisie.
    - Amélioration des actions sur les messages (menu contextuel via clic droit ou bouton dédié).
    - Amélioration de la gestion des fils de discussion (citations de messages, comptage précis des réponses).
- **Notifications et lecture** :
    - Gestion fine des niveaux de notification par discussion (tous les messages, mentions et fils suivis, ou mode silencieux).
    - Amélioration de la gestion des messages non lus (ouverture automatique au bon endroit, indicateurs visuels persistants).
- **Interface utilisateur (UI/UX)** :
    - Refonte visuelle de l'interface : bulles de message, en-têtes de discussion, panneau latéral et états vides.
    - Ajout d'un écran de chargement (splash screen) au démarrage.
    - Ajout d'un bouton "Donner un avis" pour faciliter le retour utilisateur.
    - Optimisation de l'affichage sur mobile et gestion du redimensionnement du panneau latéral.
- **Internationalisation** :
    - Support officiel du français et de l'anglais, avec synchronisation de la langue selon le profil utilisateur.

### Évolutions techniques
- **Performance et optimisation** :
    - Accélération du démarrage via le chargement parallèle des données utilisateur, du driver et de la cryptographie.
    - Utilisation de Web Workers pour la gestion du cache de synchronisation.
    - Optimisation du rendu des listes (chargement progressif des fils de discussion et rendu uniquement des conversations visibles).
    - Réduction des freezes lors de l'ouverture de conversations volumineuses.
- **Observabilité** :
    - Intégration de PostHog pour le suivi des événements d'activation, de l'utilisation des fonctionnalités de chat et des échecs de déchiffrement.
    - Exposition de métriques (ID utilisateur, version) pour l'analyse.
- **Infrastructure et CI/CD** :
    - Mise à jour des environnements Docker (support HTTPS pour la connexion Tchap, gestion des permissions utilisateurs).
    - Configuration d'un environnement de test "sandbox".
    - Amélioration de la chaîne de tests (CI) avec l'utilisation de runners Ubuntu 26.04 et d'une pile Matrix locale pour les tests de bout en bout (E2E).

### Autres changements
- **Documentation** : Mise à jour de la documentation concernant les règles de traduction et la connexion avec Tchap.
- **Maintenance** : Nettoyage du code avec Prettier et mise à jour de diverses dépendances.
