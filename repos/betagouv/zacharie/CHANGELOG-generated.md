## Changelog : zacharie (30 derniers jours, au 10/09/2026)

### Résumé
Cette période a été marquée par une optimisation importante du processus de vente et de don de carcasses, ainsi que par l'amélioration des communications par email. L'expérience utilisateur a également été affinée via des corrections d'interface, une meilleure gestion des comptes utilisateurs et de nouveaux outils de suivi pour les administrateurs.

### Évolutions fonctionnelles
- **Gestion des ventes et dons** : Ajout d'un bouton pour créer un partenaire directement depuis la section de vente [#622], mise en place d'un assistant (wizard) pour le choix des destinataires [#555], et optimisation du tri et de la sélection des carcasses (pré-sélection et séparation des catégories) [#620, #619].
- **Suivi et traçabilité** : Possibilité d'ajouter des commentaires optionnels sur les carcasses [#607], affichage du CCG du collecteur dans les détails [#612], ajout du numéro de bon de réception [#577] et amélioration des filtres d'administration pour les carcasses et les FEI [#574].
- **Gestion des utilisateurs** : Possibilité de modifier son mot de passe [#544], correction du comportement de suppression de compte lors d'un désengagement d'entité [#585] et prévention des doublons lors de la soumission d'entités [#586].
- **Communications** : Déploiement de nouveaux modèles d'emails (inscription, attribution FEI) [#592, #562] et corrections des contenus, des templates de relance et des liens de redirection dans les emails [#598, #594, #602, #595].
- **Expérience utilisateur et recherche** : Amélioration de la recherche par ville [#590] et de la barre de recherche principale [#588], ainsi que des corrections de libellés, de l'interface de sélection et du style des indicateurs de chargement [#610, #580, #609, #575].
- **Flux métier** : Mise en place d'un flux dédié à la gestion des anomalies [#523] et correction d'un blocage du SVI lors des demandes de modification de marquage [#549].

### Évolutions techniques
- **Architecture et API** : Refonte de l'API publique v1 pour aligner la gestion de la propriété sur la carcasse [#583] et renforcement de la sécurité sur les écritures de synchronisation hors périmètre [#573].
- **Automatisation et intégrations** : Optimisation de la synchronisation avec Brevo [#e3d4186, #582], gestion des notifications push natives [#584] et automatisation de la clôture des carcasses via des tâches cron [#578].
- **Infrastructure et Qualité** : Réalisation de tests de charge [#604], mise à jour des processus CI/CD [#593], correction des données analytiques [#576] et maintenance du tableau de bord Metabase [#591].

### Autres changements
- **Nettoyage** : Suppression de fonctions de résumé de carcasses obsolètes [#611] et corrections orthographiques diverses.
