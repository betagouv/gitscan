## Changelog : zacharie (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, Zacharie a franchi une étape importante avec l'intégration de la gestion de la trichine et le renforcement des outils pour les laboratoires (exports de données et ajout de photos). L'application est devenue nettement plus performante, avec un poids au chargement divisé par deux, et offre une expérience beaucoup plus fiable en mode hors ligne grâce à une gestion optimisée de la synchronisation des données.

### Évolutions fonctionnelles
- **Gestion de la trichine et laboratoires** : Mise en place de l'espace dédié à la gestion de la trichine [#596], possibilité pour les laboratoires d'exporter des données (pools, échantillons, fiches) vers leurs LIMS en CSV ou JSON [#793], et ajout de la possibilité de joindre des photos de larves aux fiches de confirmation [#788].
- **Administration et pilotage** : Amélioration des outils d'administration (création de nouveaux destinataires, gestion des invitations, accès aux tableaux de bord départementaux pour les fédérations) [#652], [#784], [#696], [#774] et nouveaux exports de bilans d'anomalies pour le SVI [#753].
- **Fiabilité et synchronisation** : Amélioration majeure de la robustesse du mode hors ligne, de la gestion des conflits de synchronisation et de la reprise de connexion [#719], [#700], [#699], [#656]. L'application supporte désormais l'utilisation dans plusieurs onglets simultanément [#772].
- **Corrections et sécurité** : Restriction de la modification des champs selon les rôles utilisateurs [#771], correction des filtres de recherche et de la fluidité des listes de carcasses [#782], [#781], [#780], et renforcement de la protection des données personnelles et des accès API [#682], [#676].

### Évolutions techniques
- **Performance** : Réduction de 50 % du poids de l'application au chargement [#643] et optimisation de la réactivité des listes et des filtres de recherche [#781], [#780].
- **Qualité et CI/CD** : Accélération des tests E2E dans la chaîne de CI [#798] et renforcement des processus de vérification automatique sur les Pull Requests [#778].
- **Observabilité** : Intégration de nouveaux événements de suivi Matomo pour affiner l'analyse de l'usage et des rôles administrateurs [#777], [#632].

### Autres changements
- **Documentation** : Rédaction de la documentation technique concernant l'audit de la synchronisation hors ligne et le processus de rechargement des données locales [#737], [#704].
