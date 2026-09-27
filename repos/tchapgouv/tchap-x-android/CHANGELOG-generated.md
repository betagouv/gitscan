## Changelog : tchap-x-android (30 derniers jours, au 24 septembre 2026)

### Résumé
Cette période a été marquée par le déploiement des versions 26.08 et 26.09, apportant des améliorations majeures à l'expérience utilisateur, notamment la possibilité d'envoyer plusieurs fichiers simultanément et une meilleure gestion du mode sombre. La sécurité a également été renforcée par l'intégration d'un scan antivirus et une gestion optimisée des certificats système.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités et améliorations :**
    - Envoi de fichiers et d'images multiples.
    - Amélioration des sondages avec la possibilité de sélectionner plusieurs réponses.
    - Nouvelles options d'interface : compteur de messages non lus, accès rapide au dernier message non lu et support étendu du thème sombre.
    - Connexion simplifiée via l'e-mail partagé depuis Tchap Classique.
- **Corrections et interface :**
    - Correction de l'affichage de la carte lors du partage de position.
    - Amélioration de la visibilité des textes (snackbar) en mode sombre.
    - Corrections sur le processus de connexion et de création de compte (LoginHint).
    - Optimisation du classement des suggestions de mentions.
    - Correction de l'affichage des badges d'information dans l'historique des salons et des erreurs de traduction ([#7612](https://github.com/tchapgouv/tchap-x-android/pull/7612)).

### Évolutions techniques
- **Sécurité et conformité :**
    - Intégration d'un scan anti-virus.
    - Activation du scanner de contenu et gestion des certificats par le système Android.
    - Masquage de l'icône d'authenticité non garantie en dehors du mode debug.
- **Performance et architecture :**
    - Optimisation du rendu des emojis pour éviter les recompositions inutiles ([#7531](https://github.com/tchapgouv/tchap-x-android/pull/7531)).
    - Améliorations et corrections du SDK Rust (support des architectures arm64 et processus de build).
    - Correction de plantages liés à la gestion d'objets circulaires lors du logging.
- **Infrastructure et CI/CD :**
    - Ajout du support de build pour F-Droid.
    - Activation des statistiques analytiques via PostHog.
    - Mise à jour des scripts de déploiement avec Fastlane.

### Autres changements
- **Documentation et support :**
    - Rédaction d'un guide pour la sauvegarde automatique de Tchap Classique.
    - Remplacement des liens vers Element par des liens vers la FAQ Tchap.
