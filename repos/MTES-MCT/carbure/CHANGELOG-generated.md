## Changelog : carbure (30 derniers jours, au 02/11/2026)

### Résumé
Ce mois a été marqué par des avancées majeures sur la gestion de la traçabilité et l'extension des fonctionnalités pour le biométhane. La plateforme offre désormais de nouveaux outils aux fournisseurs de biométhane et améliore la précision du suivi des matières (gestion des unités et des facteurs de conversion). Les outils d'administration ont également été renforcés pour permettre une gestion plus fine des utilisateurs et des droits.

### Évolutions fonctionnelles
- **Biométhane** :
  - Mise en place d'une interface dédiée aux fournisseurs de biométhane pour consulter les déclarations des producteurs liés par contrat.
  - Introduction de la possibilité de réouvrir des déclarations annuelles, avec un système de notification automatique pour les producteurs.
  - Amélioration de l'affichage des types de collecte (IAA) et de la sélection de l'année.
- **Traçabilité** :
  - Amélioration de la précision du suivi avec la gestion native des unités (masse, volume, énergie) et l'affichage des quantités avec leurs unités respectives.
  - Renforcement de la logique de traçabilité : chaque création possède désormais un statut de "naissance" et un lien de parenté explicite.
  - Meilleure visibilité des filtres de statut et affichage des périodes de travail.
- **Hydrogène (H2)** :
  - Amélioration de la visibilité pour les administrateurs industriels (consultation en lecture seule et recherche par entreprise).
  - Ajout de filtres par statut sur les lots d'hydrogène.
- **Administration & Utilisateurs** :
  - Enrichissement de la gestion des utilisateurs : filtrage par entité ou par statut actif, export des listes filtrées et consultation des droits par entité.
  - Amélioration de la visibilité des comptes (affichage du nombre total d'utilisateurs dans les récapitulatifs).
- **Biocarburants** :
  - Ajustement du périmètre IRICC pour exclure les biocarburants SAF.
  - Masquage (non suppression) des types ETBE-100 et ETBE-63.

### Évolutions techniques
- **Traçabilité & Données** :
  - Refonte de la gestion des matériaux : intégration des facteurs de conversion (LHV/PCI), de la densité et des unités directement dans le catalogue des matériaux (import via CSV).
  - Optimisation de l'import Excel pour permettre l'importation sans facteurs de conversion immédiats.
  - Amélioration de la robustesse de l'importation des données biométhane (chargement préalable du catalogue des intrants).
- **API & Architecture** :
  - Optimisation des performances et de la sécurité de l'API via l'utilisation de champs explicites dans les sérialiseurs au lieu de `__all__` [#2432](https://github.com/MTES-MCT/carbure/issues/2432).
  - Création de nouveaux endpoints API pour les fournisseurs de biométhane.
  - Refactorisation du service de réouverture des déclarations pour une meilleure maintenance.
- **Sécurité & Validation** :
  - Renforcement de la validation des données avec un contrôle du format SIREN pour les identifiants d'enregistrement [#2415](https://github.com/MTES-MCT/carbure/issues/2415).
  - Mise à jour de la gestion des certificats de sécurité (emSign).

### Autres changements
- Mise à jour du schéma de l'API.
- Nettoyage du code et extraction du module `EntityCertificate`.
