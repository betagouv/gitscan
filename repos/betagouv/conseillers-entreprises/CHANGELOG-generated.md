## Changelog : conseillers-entreprises (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment l'ajout d'informations sur l'historique des besoins des entreprises, l'amélioration de la gestion des emails de sollicitation et l'optimisation des performances. Des efforts ont également été faits pour moderniser la stack technique, notamment en remplaçant Webpack par Esbuild.

### Évolutions fonctionnelles
- Ajout de l'historique des besoins d'une entreprise, incluant les besoins inaccessibles. [#4550](https://github.com/betagouv/conseillers-entreprises/pull/4550)
- Affichage du nombre de besoins historiques sur la page d'un besoin. [#4550](https://github.com/betagouv/conseillers-entreprises/pull/4550)
- Amélioration de l'affichage des données d'évolution dans les rapports de coopération, avec un affichage en pourcentage relatif. [#4500](https://github.com/betagouv/conseillers-entreprises/pull/4500)
- Possibilité de consulter les statistiques directement depuis l'interface d'administration. [#4498](https://github.com/betagouv/conseillers-entreprises/pull/4498)
- Refonte de la gestion des emails de sollicitation :
    - Ajout d'un modèle `SolicitationMailTemplate` pour gérer les templates d'emails. [#4485](https://github.com/betagouv/conseillers-entreprises/pull/4485)
    - Amélioration de l'interface d'administration pour la gestion des templates d'emails.
    - Possibilité de personnaliser le contenu des emails de sollicitation.
    - Gestion des cas où l'API ne renvoie pas de données valides.
- Ajout d'une page "Équipe" avec les témoignages d'experts. [#4506](https://github.com/betagouv/conseillers-entreprises/pull/4506)
- Correction d'un bug empêchant la réutilisation du SIRET dans les formulaires de sollicitation. [#4524](https://github.com/betagouv/conseillers-entreprises/pull/4524)

### Évolutions techniques
- Remplacement de Webpack par Esbuild pour améliorer les performances de build et réduire la taille des assets. [#4520](https://github.com/betagouv/conseillers-entreprises/pull/4520)
- Suppression de jQuery et des dépendances associées. [#4526](https://github.com/betagouv/conseillers-entreprises/pull/4526)
- Refactorisation du code pour utiliser Turbo Frames au lieu de Turbo Streams. [#4544](https://github.com/betagouv/conseillers-entreprises/pull/4544)
- Simplification de la logique de gestion des périodes de temps (TimeDurationService). [#4519](https://github.com/betagouv/conseillers-entreprises/pull/4519)
- Mise à jour des dépendances (undici, concurrent-ruby, nokogiri, net-imap).
- Amélioration de la robustesse de la correspondance des jobs Sidekiq. [#4559](https://github.com/betagouv/conseillers-entreprises/pull/4559)
- Correction d'une vulnérabilité potentielle liée à l'injection de code. [#4514](https://github.com/betagouv/conseillers-entreprises/pull/4514)

### Autres changements
- Mise à jour de la documentation de l'architecture du projet. [#4463](https://github.com/betagouv/conseillers-entreprises/pull/4463)
- Amélioration des tests et correction de bugs mineurs.
- Nettoyage du code et suppression de code inutilisé.
- Mise à jour des traductions françaises.
- Configuration de rails-erd pour générer des PDFs. [#4537](https://github.com/betagouv/conseillers-entreprises/pull/4537)
- Ajustement des valeurs de timeout de la base de données. [#4537](https://github.com/betagouv/conseillers-entreprises/pull/4537)
