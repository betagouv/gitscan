## Changelog : srdt (30 derniers jours, au 21/10/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la précision et de la flexibilité de la recherche juridique. Les utilisateurs bénéficient désormais d'une meilleure gestion des jurisprudences, de liens directs vers les articles de loi et d'une navigation plus fluide, notamment grâce à la possibilité de rendre la recherche jurisprudentielle optionnelle et à la correction de certains flux d'authentification.

### Évolutions fonctionnelles
- **Recherche et précision juridique**
    - Amélioration de la gestion et de la qualité des jurisprudences.
    - La recherche jurisprudentielle peut désormais être rendue optionnelle [#437](https://github.com/SocialGouv/srdt/issues/437).
    - Ajout de liens directs vers les articles de loi [#322](https://github.com/SocialGouv/srdt/issues/322) ([#430](https://github.com/SocialGouv/srdt/issues/430)).
    - Correction de l'ordre d'affichage des résultats de recherche pour respecter le réordonnancement (rerank).
    - Amélioration de la prise en charge des liens vers le Code du travail sur Légifrance [#404](https://github.com/SocialGouv/srdt/issues/404) ([#420](https://github.com/SocialGouv/srdt/issues/420)).
- **Navigation et accès**
    - Correction du processus de déconnexion via ProConnect pour assurer un fonctionnement correct côté serveur [#438](https://github.com/SocialGouv/srdt/issues/438).

### Évolutions techniques
- Optimisation de la recherche de proximité (k-NN) au niveau de l'API pour de meilleures performances de recherche.
- Renforcement des mécanismes d'anonymisation des données et amélioration de la qualité des journaux d'événements (logs).
