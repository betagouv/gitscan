## Changelog : rdv-service-public (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la migration vers un nouveau nom de domaine, l'amélioration de l'expérience utilisateur (notamment avec l'intégration du Design System de l'État - DSFR), et la correction de plusieurs bugs liés à la synchronisation CalDAV, aux rendez-vous et à l'interface utilisateur. Des améliorations de sécurité et de performance ont également été apportées.

### Évolutions fonctionnelles
- **Nouveau nom de domaine :** Plusieurs corrections et ajustements ont été effectués pour assurer une transition fluide vers le nouveau nom de domaine, incluant la redirection des utilisateurs et la mise à jour de la documentation.
- **Réservation en ligne :** Ajout de liens entre les détails du motif et la réservation en ligne [#6466].
- **Rendez-vous d'accompagnement :** Désactivation des rendez-vous d'accompagnement pour certains espaces [#6435].
- **Synchronisation CalDAV :** Amélioration de la synchronisation CalDAV avec Zimbra [#6417] et correction de bugs liés à l'activation des données personnelles et à l'import d'événements [#6488, #6416].
- **Interface utilisateur :**
    - Remplacement progressif des composants Bootstrap par des composants du Design System de l'État (DSFR) : boutons [#6468, #6469], badges [#6467], alertes [#6489], cartes [#6437, #6416], accordéons [#6434].
    - Amélioration de l'accessibilité (a11y) : correction du focus sur les éléments de navigation de l’agenda [#6499] et ajout de liens explicites [#6498].
    - Ajout d'une flèche sur les cards de motifs pour une meilleure découvrabilité [#6429].
    - Affichage du nom de l'usager connecté [#6452].
- **Gestion des organisations :** Possibilité pour les administrateurs d'espace de créer un nouveau service [#6455].
- **Création de comptes :** Correction de bugs liés à la création de comptes sur le nouveau nom de domaine [#6484] et amélioration du parcours d'onboarding [#6486].
- **Motifs :** Ajout d'une étape de sélection d'agenda pour la synchronisation CalDAV [#6172] et correction d'un bug de retrait de catégorie [#6478].

### Évolutions techniques
- **Refactoring CSS :** Réduction de la dépendance à Bootstrap pour une meilleure maintenabilité [#6457].
- **Recherche par téléphone/ID :** Suppression de la dépendance à `tsvector` pour la recherche par téléphone et ID, améliorant ainsi la performance [#6349].
- **GoodJob :** Correction d'un problème lié à la gestion des jobs GoodJob [#6408].
- **ActionCable :** Correction de tests flaky liés à ActionCable [#6426].
- **Mise à jour des dépendances :**
    - Puma (6.4.3 -> 7.2.1) [#6425]
    - Esbuild (0.27.3 -> 0.28.1) [#6438]
    - net-imap (0.5.14 -> 0.5.15) [#6441]
- **Scripts :** Amélioration du script pour merger des agents [#6475] et ajout d'un script pour créer 29 motifs France Service [#6406].
- **Sécurité :** Fixation par hash des versions des actions GitHub [#6412].

### Autres changements
- **Documentation :** Mise à jour de la documentation et des mentions légales pour le nouveau nom de domaine [#6442, #6413].
- **Configuration :** Ajout d'un fichier `mise.toml` et mise à jour des instructions d'installation [#6440].
- **Sécurité des agents :** Marquer comme sensibles les agents des organisations rdv-insertion [#6387].
- **Tests :** Amélioration des tests et correction de valeurs filtrées dans les tests RSpec [#6453].
- **Nettoyage de code :** Suppression de code inutilisé et de commentaires obsolètes [#6423, #6445].
- **Sentry :** Ajout d'envoi de debug à Sentry lors d'erreurs Caldav au setup initial [#6424].
