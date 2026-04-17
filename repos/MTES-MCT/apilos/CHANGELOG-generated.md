## Changelog : apilos (30 derniers jours, au 15 mai 2026)

### Résumé
Cette version apporte des améliorations de performance significatives, notamment dans la récupération des données de logements. De nouvelles fonctionnalités permettent l'export des conventions départementales directement vers S3, facilitant ainsi l'archivage et le partage. Des corrections de bugs et des ajustements ont également été effectués pour améliorer la stabilité et la qualité du service.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les conventions départementales vers un bucket S3. [#2151](https://github.com/MTES-MCT/apilos/issues/2151)
- Correction de l'affichage de l'adresse sur le template Word FicheCAF. [#2141](https://github.com/MTES-MCT/apilos/issues/2141)
- Suppression de la mention "beta.gouv" du bas de page du site. [#2145](https://github.com/MTES-MCT/apilos/issues/2145)
- Correction de la correspondance entre les logements et leurs financements. [#2140](https://github.com/MTES-MCT/apilos/issues/2140)

### Évolutions techniques
- Optimisation de la récupération des logements grâce au préchargement et à la mise en cache. [#2155](https://github.com/MTES-MCT/apilos/issues/2155)
- Augmentation du nombre de workers Gunicorn pour améliorer la capacité de traitement. [#2154](https://github.com/MTES-MCT/apilos/issues/2154)
- Ajustement du délai d'expiration de Gunicorn pour une meilleure gestion des requêtes. [#2153](https://github.com/MTES-MCT/apilos/issues/2153) et [#2146](https://github.com/MTES-MCT/apilos/issues/2146)
- Implémentation de la commande d'export des conventions et mise à jour de la documentation associée. [#2149](https://github.com/MTES-MCT/apilos/issues/2149)
- Ajout de logs d'avertissement pour la fonction de calcul des KPI. [#2142](https://github.com/MTES-MCT/apilos/issues/2142)
- Suppression des logs d'avertissement inutiles de la classe ConventionKPI. [#2148](https://github.com/MTES-MCT/apilos/issues/2148)
