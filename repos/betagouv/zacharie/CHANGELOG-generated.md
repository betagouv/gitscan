## Changelog : zacharie (30 derniers jours, au 20 octobre 2026)

### Résumé
Ce mois-ci, Zacharie a franchi une étape majeure avec l'intégration complète de la gestion de la trichine et le renforcement de la traçabilité grâce à un historique détaillé de toutes les modifications. L'application est devenue nettement plus performante et robuste, notamment pour les utilisateurs travaillant en mode hors ligne ou gérant de gros volumes de données, tout en bénéficiant de renforcements de sécurité importants.

### Évolutions fonctionnelles

**Gestion de la trichine et laboratoires**
- Mise en place d'un espace dédié à la gestion de la trichine [#596].
- Possibilité pour les laboratoires d'exporter leurs données (pools, échantillons, fiches) aux formats CSV ou JSON pour leur LIMS [#793].
- Amélioration de la visibilité pour les laboratoires : consultation des fiches de confirmation envoyées au LNR et possibilité d'y joindre des photos de larves [#788].
- Sécurisation des résultats : les résultats de trichine ne peuvent désormais être transmis que via l'application et non plus par email [#806].

**Traçabilité et gestion des données**
- Introduction d'un historique complet des versions pour les fiches, les carcasses, les utilisateurs et les entités [#755].
- Capacité pour le SVI et l'administration d'exporter le bilan des anomalies de fin de saison [#753].
- Amélioration de la gestion des destinataires : création de nouveaux destinataires (commerce, cantine, etc.) depuis l'interface admin [#652] et possibilité pour un chasseur d'ajouter un collecteur professionnel comme destinataire [#659].

**Administration et supervision**
- Amélioration des outils de supervision : accès des fédérations nationales et régionales aux tableaux de bord départementaux [#696] et affichage du nombre de carcasses/fiches par utilisateur pour les superadmins [#663].
- Optimisation de la gestion des utilisateurs : création de liens d'invitation par les administrateurs [#784] et ajout d'une vue "destinataire" sur les fiches [#774].

**Expérience utilisateur et synchronisation**
- Optimisation majeure de la synchronisation hors ligne : meilleure gestion des conflits, reprise automatique après une coupure réseau et affichage immédiat des modifications locales dans les listes [#752, 719, 707, 701, 700, 699, 656].
- Amélioration de la fluidité : les listes et les filtres de recherche sont désormais beaucoup plus rapides, même avec un grand nombre de carcasses [#781, 782, 780, 643].
- Correction de nombreux comportements d'interface (menus déroulants, suggestions de saisie sur iOS, gestion des erreurs de saisie) pour éviter les plantages de l'application [#768, 658, 645, 759].

### Évolutions techniques

**Performance et infrastructure**
- Optimisation du poids de l'application : le volume de données chargé au démarrage a été divisé par deux [#643].
- Accélération de la chaîne de tests : la CI (intégration continue) pour les tests de bout en bout (E2E) démarre plus rapidement grâce à une meilleure gestion du cache et de Chromium [#798].

**Sécurité**
- Protection des données sensibles : les mots de passe, jetons de session et données personnelles ne sont plus transmis dans les logs ou vers Sentry [#682].
- Renforcement de la sécurité de l'API : obligation de définir un secret de session en production [#671] et limitation des tentatives de connexion [#673].
- Sécurisation des accès : protection contre les redirections vers des sites externes malveillants [#678] et restriction des droits de modification des champs selon les rôles utilisateurs [#771].
- Nettoyage de sécurité : retrait de dépendances inutilisées présentant des vulnérabilités (notamment `matrix-js-sdk`) [#6f36e25].

### Autres changements
- Documentation technique : rédaction de la documentation concernant l'audit de la synchronisation hors ligne et le rechargement des données locales [#737, 704].
- Mise à jour des mentions légales pour inclure l'utilisation de Brevo pour l'envoi des courriels [#800].
