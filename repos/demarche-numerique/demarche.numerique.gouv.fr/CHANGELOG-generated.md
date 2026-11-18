## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 17/11/2026)

### Résumé
Cette période a été marquée par une modernisation importante de l'expérience utilisateur et de la sécurité. Les évolutions majeures incluent l'introduction de FranceConnect+, une gestion plus transparente des sessions de connexion et une refonte des outils d'administration (notamment pour la gestion des jetons API et le suivi de la santé des services externes). La plateforme est également devenue plus robuste grâce à une amélioration des processus d'exportation de données et à une gestion plus fine de l'archivage des dossiers.

### Évolutions fonctionnelles
- **Authentification et Sessions**
  - Introduction de FranceConnect+ avec gestion sécurisée des tokens et déchiffrement RSA. [#14475](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14475)
  - Amélioration de la visibilité des sessions : la méthode de connexion (mot de passe, FranceConnect, ProConnect) est désormais affichée dans le menu utilisateur.
  - Amélioration du parcours de fusion de comptes FranceConnect pour éviter les demandes de mot de passe redondantes. [#14589](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14589)
- **Gestion du Profil et Sécurité**
  - Possibilité pour les utilisateurs connectés de modifier leur mot de passe. [#13782](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13782)
  - Mise en place d'un mécanisme de limitation (throttling) des tentatives de changement de mot de passe.
- **Administration et Pilotage**
  - Création d'un tableau de bord de suivi pour l'API Entreprise, permettant de visualiser les pannes et les états de dégradation des services. [#14383](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14383)
  - Refonte de l'interface de gestion des jetons API : ajout de la duplication de jetons, de badges d'expiration et d'une sélection multiple plus ergonomique. [#14425](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14425)
  - Nouvelle fonctionnalité de comparaison de champs (champ matching) pour faciliter l'analyse entre deux procédures. [#14420](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14420)
  - Gestion plus fine des restrictions de domaines d'email pour les instructeurs. [#14412](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14412)
- **Gestion des Dossiers et Expertise**
  - Nouveau système d'avertissement avant l'archivage des dossiers (individuel ou en masse) pour éviter les erreurs de manipulation. [#14459](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14459)
  - Amélioration de l'aperçu des attestations avec un sélecteur de dossier regroupé par révision. [#14459](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14459)
  - Affichage du nombre d'avis donnés directement à côté du lien de consultation pour les experts. [#14393](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14393)
  - Ajout d'un tag "Date et heure de décision" pour le suivi des dossiers. [#14311](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14311)
- **Exports et Documents**
  - Amélioration de la fiabilité des exports Excel et CSV (gestion des apostrophes, des formules et des caractères spéciaux). [#14579](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14579)

### Évolutions techniques
- **Architecture et Refactoring**
  - Migration massive des templates de la plateforme de HAML vers ERB pour une meilleure maintenance. [#14576](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14576)
  - Migration de la chaîne d'outils front-end vers Vite+. [#14031](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14031)
  - Suppression définitive de l'API v1 au profit de la v2. [#9999](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/9999)
  - Optimisation de la structure GraphQL, notamment sur la gestion des descripteurs de champs.
- **Sécurité et CI/CD**
  - Renforcement de la sécurité des jetons API via l'utilisation de digests SHA-256. [#14368](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14368)
  - Mise en place de la vérification des signatures GPG des commits dans la file d'attente de fusion (merge queue). [#14534](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14534)
- **Performances**
  - Optimisation du streaming pour le téléchargement des dossiers compressés (ZIP). [#14371](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14371)
  - Optimisation des processus d'exportation et de la gestion des champs répétitifs.

### Autres changements
- Documentation mise à jour pour l'API et les services de staging.
- Nettoyage de la base de code (suppression de nombreux flags de fonctionnalités obsolètes).
