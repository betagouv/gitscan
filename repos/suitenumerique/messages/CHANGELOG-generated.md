## Changelog : messages (30 derniers jours, au 10 septembre 2026)

### Résumé
Ce mois-ci, les développements se sont concentrés sur le renforcement de la sécurité (protection du serveur de mail, accès administrateur) et l'extension des capacités de gestion pour les administrateurs (export de données, gestion DNS). L'expérience utilisateur a également été affinée, notamment sur mobile et via une meilleure gestion des adresses e-mail internationales.

### Évolutions fonctionnelles
- **Administration** : Ajout de la possibilité d'exporter des boîtes mail pour les administrateurs de domaine [#789](https://github.com/suitenumerique/messages/issues/789) et de lister les enregistrements DNS pour l'ensemble des domaines [#780](https://github.com/suitenumerique/messages/issues/780).
- **Messagerie** : Support des adresses e-mail internationales (i18n) et normalisation automatique des boîtes mail en minuscules [#785](https://github.com/suitenumerique/messages/issues/785).
- **Interface utilisateur** : Amélioration de l'affichage des extraits de messages et de l'expéditeur dans les fils de discussion, et masquage des statistiques du dossier "Envoyés".
- **Statistiques** : Les messages classés comme spam ou déplacés vers la corbeille sont désormais exclus par défaut des statistiques.
- **Mobile** : Amélioration du processus de déconnexion pour garantir la fermeture complète de la session d'identité.

### Évolutions techniques
- **Sécurité** : Renforcement du composant de transport de mail (pymta) avec de nouvelles limites et paramètres [#777](https://github.com/suitenumerique/messages/issues/777) et amélioration de la précision du vérificateur SPF [#782](https://github.com/suitenumerique/messages/issues/782).
- **Sécurité** : Mise en place d'une liste blanche d'adresses IP pour l'accès à l'administration Django et durcissement des workflows GitHub Actions.
- **Backend** : Optimisation du MTA (pymta) concernant la gestion des variables d'environnement, la cohérence et la journalisation (logging) [#783](https://github.com/suitenumerique/messages/issues/783).
- **Mobile** : Migration de la configuration de l'identité et du schéma d'authentification vers un système piloté par les variables d'environnement.

### Autres changements
- **Documentation** : Ajout d'un guide de configuration pour le fournisseur d'identité [#781](https://github.com/suitenumerique/messages/issues/781).
