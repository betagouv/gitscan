## Changelog : bhasile (30 derniers jours, au 02/11/2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'une amélioration notable de son interface utilisateur, avec une navigation simplifiée, des outils de recherche et de filtrage plus performants et une cartographie enrichie. Les fonctionnalités de statistiques ont été fiabilisées et la sécurité a été renforcée, notamment via l'imposition de l'authentification multi-facteurs (MFA) et une gestion plus fine des rôles.

### Évolutions fonctionnelles
- **Interface et navigation** : Mise en place d'un nouveau menu ([#1751](https://github.com/betagouv/bhasile/issues/1751)), d'un nouveau design pour l'import des documents financiers ([#1724](https://github.com/betagouv/bhasile/issues/1724)) et ajout d'un lien vers le centre d'aide ([#1699](https://github.com/betagouv/bhasile/issues/1699)).
- **Cartographie** : Ajout de la localisation par adresse ([#1680](https://github.com/betagouv/bhasile/issues/1680)) et affichage des lieux d'hébergement au niveau communal ([#1686](https://github.com/betagouv/bhasile/issues/1686)).
- **Recherche et filtres** : Unification des filtres ([#1739](https://github.com/betagouv/bhasile/issues/1739)), ajout de la recherche par département ([#1700](https://github.com/betagouv/bhasile/issues/1700)) et possibilité de filtrer par subventions ([#1721](https://github.com/betagouv/bhasile/issues/1721)).
- **Statistiques et données** : Amélioration des statistiques pour les années incomplètes ([#1705](https://github.com/betagouv/bhasile/issues/1705)), correction de données statistiques ([#1697](https://github.com/betagouv/bhasile/issues/1697)) et réalignement des statistiques publiques ([#1708](https://github.com/betagouv/bhasile/issues/1708), [#1709](https://github.com/betagouv/bhasile/issues/1709)).
- **Gestion métier** : Évolution de la logique des CPOM régionaux ([#1737](https://github.com/betagouv/bhasile/issues/1737)), possibilité de rendre les indicateurs financiers optionnels dans les CPOM ([#1717](https://github.com/betagouv/bhasile/issues/1717)) et maintien des structures fermées dans les descriptions ([#1707](https://github.com/betagouv/bhasile/issues/1707)).
- **Nettoyage de l'interface** : Suppression de certains éléments (filiales [#1723](https://github.com/betagouv/bhasile/issues/1723), note moyenne [#1696](https://github.com/betagouv/bhasile/issues/1696), coût cible [#1758](https://github.com/betagouv/bhasile/issues/1758)) et du formulaire de récupération d'adresses ([#1716](https://github.com/betagouv/bhasile/issues/1716)).

### Évolutions techniques
- **Sécurité et accès** : Renforcement de l'authentification MFA sur ProConnect ([#1712](https://github.com/betagouv/bhasile/issues/1712)), évolution de la gestion des rôles et des périmètres ([#1694](https://github.com/betagouv/bhasile/issues/1694)) et amélioration de la vérification du statut d'agent ([#1748](https://github.com/betagouv/bhasile/issues/1748)).
- **Infrastructure et Framework** : Mise à jour de Next.js ([#1740](https://github.com/betagouv/bhasile/issues/1740)), migration des ressources vers S3 ([#1661](https://github.com/betagouv/bhasile/issues/1661)) et configuration de Sentry pour la production uniquement ([#1753](https://github.com/betagouv/bhasile/issues/1753)).
- **Qualité et Tests** : Corrections importantes des tests unitaires et de bout en bout (e2e) ([#1725](https://github.com/betagouv/bhasile/issues/1725), [#1726](https://github.com/betagouv/bhasile/issues/1726), [#1727](https://github.com/betagouv/bhasile/issues/1727), [#1762](https://github.com/betagouv/bhasile/issues/1762)).
- **Backend et API** : Correction des tâches planifiées (crons) ([#1750](https://github.com/betagouv/bhasile/issues/1750)), contrôle accru des routes API pour les CPOM et opérateurs ([#1731](https://github.com/betagouv/bhasile/issues/1731)) et amélioration des logs pour les problèmes de fichiers ([#1732](https://github.com/betagouv/bhasile/issues/1732)).
- **Refactoring** : Refonte de la structure de la carte ([#1681](https://github.com/betagouv/bhasile/issues/1681)).

### Autres changements
- **Documentation** : Amélioration de la FAQ ([#1729](https://github.com/betagouv/bhasile/issues/1729)).
- **Divers** : Correction de diverses coquilles ([#1730](https://github.com/betagouv/bhasile/issues/1730)) et suppression de scripts de post-déploiement ([#1756](https://github.com/betagouv/bhasile/issues/1756)).
