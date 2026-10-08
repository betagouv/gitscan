## Changelog : zacharie (30 derniers jours, au 07/10/2026)

### Résumé
Ce mois-ci, les développements se sont concentrés sur la robustesse du mode hors ligne, la sécurisation des données utilisateurs et l'amélioration des outils de pilotage pour les fédérations. L'application est désormais plus légère, plus sûre et offre une expérience de saisie sur le terrain plus fluide et fiable.

### Évolutions fonctionnelles
- **Mode hors ligne et synchronisation** : Amélioration significative de la fiabilité (persistance des saisies lors des mises à jour ou des déconnexions, gestion des conflits de versions, reprise automatique de la connexion après une coupure) et optimisation du stockage local [#709, #700, #699, #702, #705].
- **Sécurité et gestion des accès** : Renforcement des contrôles (changement d'email sécurisé par mot de passe, gestion stricte des droits d'administration, protection contre les liens malveillants) et protection de la vie privée (exclusion des données sensibles des logs et de Sentry) [#750, #748, #682, #680, #678, #671].
- **Évolutions métier** : Nouveaux tableaux de bord pour les fédérations nationales et régionales [#696], amélioration du parcours de vente/don (gestion des destinataires et des carcasses) [#620, #614, #652], et enrichissement des exports Excel [#683].
- **Expérience utilisateur (UI/UX)** : Optimisation de l'ergonomie mobile, amélioration des formulaires de saisie (suggestions de communes, dates, espèces) et corrections de l'affichage [#639, #658, #645, #647].

### Évolutions techniques
- **Performance** : Réduction de 50 % du poids de l'application au chargement [#643] et optimisation des lectures disque pour améliorer la réactivité [#742].
- **Architecture** : Optimisation du stockage des données hors ligne pour les comptes professionnels (ETG, SVI, collecteurs) afin d'alléger l'empreinte mémoire [#709].

### Autres changements
- Documentation technique (audit de la synchronisation hors ligne et du rechargement des données locales) [#737, #704].
- Maintenance (nettoyage des dépendances inutilisées) [#751].
