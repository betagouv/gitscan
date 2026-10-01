## Changelog : api-engagement (30 derniers jours, au 30/09/2026)

### Résumé
Ce mois-ci, la plateforme a connu une refonte visuelle majeure de son parcours utilisateur, notamment sur les pages de résultats, le quiz et les pages d'accueil. Le moteur de recommandation a été optimisé pour offrir des résultats plus pertinents, tandis que les capacités d'analyse de données ont été considérablement renforcées pour permettre un meilleur suivi des campagnes et des parcours utilisateurs. Enfin, des efforts importants ont été portés sur l'accessibilité (RGAA) et la sécurité des accès.

### Évolutions fonctionnelles
- **Refonte de l'interface utilisateur** : Nouveau design des pages de résultats (cartes, carte interactive, pagination) [#1401](https://github.com/betagouv/api-engagement/pull/1401), [#1399](https://github.com/betagouv/api-engagement/pull/1399) et mise à jour des pages d'accueil "defis-engagement" [#1494](https://github.com/betagouv/api-engagement/pull/1494), [#1467](https://github.com/betagouv/api-engagement/pull/1467).
- **Amélioration du parcours Quiz** : Déploiement du nouveau flux de quiz (v3) avec des options par étapes versionnées [#1451](https://github.com/betagouv/api-engagement/pull/1451).
- **Optimisation de la recherche** : Amélioration des filtres de missions (domaines, activités, tranches d'âge) [#1483](https://github.com/betagouv/api-engagement/pull/1483), [#1429](https://github.com/betagouv/api-engagement/pull/1429).
- **Sécurité et expérience utilisateur** : 
    - Ajout de l'authentification multi-facteurs (MFA) par email pour la connexion au back-office [#1472](https://github.com/betagouv/api-engagement/pull/1472).
    - Introduction de modales de confirmation pour la gestion des clés API [#1503](https://github.com/betagouv/api-engagement/pull/1503).
    - Intégration du chat Crisp avec gestion du consentement utilisateur [#1477](https://github.com/betagouv/api-engagement/pull/1477), [#1502](https://github.com/betagouv/api-engagement/pull/1502).
- **Accessibilité** : Mise en conformité RGAA du tableau de bord [#1504](https://github.com/betagouv/api-engagement/pull/1504) et publication de la déclaration d'accessibilité [#1463](https://github.com/betagouv/api-engagement/pull/1463).

### Évolutions techniques
- **Moteur de matching** : Refonte de l'algorithme de recommandation [#1500](https://github.com/betagouv/api-engagement/pull/1500), définition de nouvelles règles de scoring utilisateur [#1479](https://github.com/betagouv/api-engagement/pull/1479) et optimisation du scoring pour les missions de sécurité et de télétravail [#1433](https://github.com/betagouv/api-engagement/pull/1433), [#1432](https://github.com/betagouv/api-engagement/pull/1432).
- **Analytics et suivi** : Enrichissement massif du tracking (canaux d'acquisition, campagnes UTM, tunnels de conversion, sessions de quiz et indicateurs clés pour les éditeurs) [#1508](https://github.com/betagouv/api-engagement/pull/1508), [#1476](https://github.com/betagouv/api-engagement/pull/1476), [#1465](https://github.com/betagouv/api-engagement/pull/1465), [#1460](https://github.com/betagouv/api-engagement/pull/1460), [#1413](https://github.com/betagouv/api-engagement/pull/1413).
- **API et données** : 
    - Prise en charge des coordonnées géographiques dans les payloads de missions [#1511](https://github.com/betagouv/api-engagement/pull/1511).
    - Amélioration des requêtes d'enrichissement de géolocalisation [#1510](https://github.com/betagouv/api-engagement/pull/1510).
    - Automatisation du calcul de diffusion des missions lors des changements chez les éditeurs [#1492](https://github.com/betagouv/api-engagement/pull/1492).
- **Infrastructure et CI/CD** : 
    - Mise en place d'un nouveau workflow de sécurité [#1395](https://github.com/betagouv/api-engagement/pull/1395).
    - Automatisation de l'envoi des alertes Sentry vers Slack [#1388](https://github.com/betagouv/api-engagement/pull/1388).
    - Sécurisation des webhooks contre les requêtes non authentifiées [#1481](https://github.com/betagouv/api-engagement/pull/1481).
- **SEO** : Ajout des fichiers `robots.txt` et `sitemap.xml` pour une meilleure indexation [#1509](https://github.com/betagouv/api-engagement/pull/1509).

### Autres changements
- Mise à jour de la bibliothèque de composants DSFR [#1446](https://github.com/betagouv/api-engagement/pull/1446).
- Actualisation des données relatives aux missions ROC.
