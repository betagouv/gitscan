## Changelog : tchap-x-android (30 derniers jours, au 06/11/2026)

### Résumé
Ce mois a été marqué par le déploiement des versions 26.10 et 26.11. Les évolutions majeures concernent une meilleure gestion du multi-compte (visibilité des messages non lus et du statut des autres comptes), un système de notifications plus intelligent et des fonctionnalités de messagerie enrichies comme l'édition de messages. L'application est également devenue plus fluide grâce à d'importantes optimisations techniques visant à libérer le processeur principal.

### Évolutions fonctionnelles
- **Gestion multi-compte** : Amélioration de la visibilité avec l'affichage du statut des autres comptes dans les paramètres, ainsi que du nombre de messages non lus sur l'écran d'accueil [#7891, #7922].
- **Notifications** : 
    - Possibilité de recevoir les notifications des autres sessions sur un même appareil [#7977].
    - Nettoyage automatique des notifications pour les discussions déjà lues.
    - Ajout d'un compteur global de notifications non lues sur l'écran d'accueil [#7891].
- **Messagerie et contenu** :
    - Support de l'édition et de la suppression de messages [#7840].
    - Affichage des légendes de médias en format HTML [#7970].
    - Suggestions de salons lors du transfert de contenu.
- **Interface utilisateur** :
    - Nouvelle expérience de recherche dans la sélection de salons (remplacement de la barre de recherche par un champ dédié).
    - Affichage d'une alerte lors de la saisie d'une adresse email externe.
    - Amélioration de l'affichage des avatars et de la sélection de la timeline.
- **Transfert de messages** : Limitation du transfert multiple à 5 salons avec l'ajout d'un indicateur de confirmation visuelle.

### Évolutions techniques
- **Performance et fluidité** : Optimisation majeure de la réactivité de l'application en déportant de nombreuses opérations lourdes hors du thread principal (accès à la base de données, gestion des médias, recherche en arrière-plan, profils utilisateurs et historique des notifications).
- **Architecture** : 
    - Refonte de la gestion du changement de compte au sein de la structure de navigation.
    - Amélioration de la structure du code via la création de fonctions composables pour plus de clarté.
- **SDK et dépendances** : Mises à jour importantes du SDK Matrix Rust et ajustements sur l'intégration d'Element Call.
- **CI/CD** : Optimisation des processus de build (réduction de la taille du cache Gradle et amélioration de la résilience des tests en cas d'échec de tâche).

### Autres changements
- Mise à jour des captures d'écran de l'application.
- Synchronisation des traductions via Localazy.
- Configuration des URLs Sentry pour le suivi des erreurs.
