## Changelog : api-engagement (30 derniers jours, au 15 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'API et à la plateforme d'engagement, notamment en matière de suivi analytique, de sécurité, de performance et d'expérience utilisateur. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et la fiabilité du système. L'intégration avec Demarches Simplifiées est également finalisée.

### Évolutions fonctionnelles
- Ajout de liens entre les clics sur les missions et le classement backend pour une meilleure analyse de l'engagement des utilisateurs. [#1272](https://github.com/betagouv/api-engagement/issues/1272)
- Amélioration de l'accessibilité de l'application pour répondre aux normes RGAA 7.5 (annonces du nombre total de missions). [#1265](https://github.com/betagouv/api-engagement/issues/1265)
- Ajout de compétences Etalab pour enrichir les profils utilisateurs. [#1271](https://github.com/betagouv/api-engagement/issues/1271)
- Amélioration de la correspondance des missions distantes en utilisant un poids géographique. [#1260](https://github.com/betagouv/api-engagement/issues/1260)
- Ajout de pages légales et de liens dans le pied de page de la plateforme. [#1246](https://github.com/betagouv/api-engagement/issues/1246)
- Intégration de l'API avec Demarches Simplifiées. [#1229](https://github.com/betagouv/api-engagement/issues/1229) et [#1154](https://github.com/betagouv/api-engagement/issues/1154)
- Ajout d'un filtre "dispositif" pour les missions sur la plateforme. [#1211](https://github.com/betagouv/api-engagement/issues/1211)
- Ajout de badges de compensation sur la plateforme. [#1173](https://github.com/betagouv/api-engagement/issues/1173)
- Ajout de la possibilité de suivre les vues de pages sur la plateforme. [#1235](https://github.com/betagouv/api-engagement/issues/1235)
- Ajout de paramètres UTM aux événements de suivi. [#1255](https://github.com/betagouv/api-engagement/issues/1255)
- Ajout d'un filtre pour les missions avec un dispositif spécifique. [#1211](https://github.com/betagouv/api-engagement/issues/1211)

### Évolutions techniques
- Suppression des informations sensibles (hash de mot de passe, tokens) des réponses de l'API. [#1266](https://github.com/betagouv/api-engagement/issues/1266) et [#1265](https://github.com/betagouv/api-engagement/issues/1265)
- Restriction de la création de règles de diffusion aux opérateurs supportés. [#1264](https://github.com/betagouv/api-engagement/issues/1264)
- Amélioration des performances de la correspondance des missions avec un script de benchmark. [#1268](https://github.com/betagouv/api-engagement/issues/1268)
- Ajout de contrôles d'accès pour les modérateurs sur les routes de recherche de modération. [#1261](https://github.com/betagouv/api-engagement/issues/1261)
- Mise en place d'une nouvelle version de l'API (v4) avec la définition de la version actuelle du prompt dans l'environnement. [#1248](https://github.com/betagouv/api-engagement/issues/1248)
- Refactorisation de l'utilisation des tables `publisher_diffusion`. [#1135](https://github.com/betagouv/api-engagement/issues/1135) et [#1206](https://github.com/betagouv/api-engagement/issues/1206)
- Utilisation de Typesense multi-search pour améliorer les performances de recherche. [#1200](https://github.com/betagouv/api-engagement/issues/1200)
- Ajout de suivi analytique avec Posthog. [#1174](https://github.com/betagouv/api-engagement/issues/1174) et [#1218](https://github.com/betagouv/api-engagement/issues/1218)
- Amélioration de la gestion des règles de diffusion des éditeurs. [#1187](https://github.com/betagouv/api-engagement/issues/1187)
- Mise à jour des dépendances et des outils de développement.

### Autres changements
- Mise à jour de la documentation des règles de diffusion. [#1177](https://github.com/betagouv/api-engagement/issues/1177)
- Ajout d'un script pour générer automatiquement le changelog. [#1202](https://github.com/betagouv/api-engagement/issues/1202)
- Corrections de bugs et améliorations de l'interface utilisateur sur la plateforme.
- Suppression d'un workflow Claude.
- Suppression de l'endpoint stats-mean.
- Correction d'un problème de prise de contrôle de compte lors de l'inscription. [#1253](https://github.com/betagouv/api-engagement/issues/1253)
- Correction d'un problème de limite de débit dans les erreurs Sentry. [#1259](https://github.com/betagouv/api-engagement/issues/1259)
- Correction de l'affichage des filtres radio des missions sur mobile. [#1234](https://github.com/betagouv/api-engagement/issues/1234)
