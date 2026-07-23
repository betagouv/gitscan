## Changelog : passemarche (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment la possibilité de télécharger une synthèse PDF de la configuration, de gérer les listes de lots volumineuses et de re-candidater à un marché avant la date limite. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger une synthèse PDF de la configuration acheteur. [#452](https://github.com/datagouv/passemarche/pull/452)
- Implémentation de l'affichage des badges de type (travaux, services, fournitures) dans l'attestation acheteur et dans le wizard candidat. [#447](https://github.com/datagouv/passemarche/pull/447)
- Amélioration de la gestion des listes de lots volumineuses avec un affichage collapsible. [#419](https://github.com/datagouv/passemarche/pull/419)
- Possibilité pour un candidat de re-candidater à un marché avant la date limite, avec gestion du blocage si la deadline est dépassée. [#438](https://github.com/datagouv/passemarche/pull/438)
- Affichage des icônes de scope (type de marché) dans les PDFs générés par wkhtmltopdf. [#450](https://github.com/datagouv/passemarche/pull/450)
- Ajout de la possibilité de modifier la deadline d'un marché dans le fake editor.
- Amélioration de l'affichage des badges de type dans la configuration des lots acheteur. [#459](https://github.com/datagouv/passemarche/pull/459)
- Organisation du dossier ZIP des documents par type de lot. [#444](https://github.com/datagouv/passemarche/pull/444)

### Évolutions techniques
- Sécurisation de la construction des URLs en utilisant un host canonique. [#460](https://github.com/datagouv/passemarche/pull/460)
- Correction d'un problème de persistance des motifs d'exclusion. [#467](https://github.com/datagouv/passemarche/pull/467)
- Correction de la gestion des liaisons orphelines lors de la migration `market_attribute_selections`. [#469](https://github.com/datagouv/passemarche/pull/469)
- Suppression de code mort (MarketApplication#find_authorized_document). [#468](https://github.com/datagouv/passemarche/pull/468)
- Historisation des modifications de lots avec PaperTrail.
- Historisation de la sélection des attributs par marché.
- Bloquage de la candidature tant que le marché n'est pas publié.
- Amélioration de la gestion des erreurs API dans le fake editor. [#470](https://github.com/datagouv/passemarche/pull/470)
- Correction de l'affichage des marchés publiés côté candidat dans le fake editor. [#471](https://github.com/datagouv/passemarche/pull/471)

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés.
- Suppression de dossiers de documentation dupliqués.
- Mise à jour des dépendances : rubyzip, simplecov, aws-sdk-s3, cucumber-rails, thruster, pagy, selenium-webdriver.
- Correction de problèmes de tests (flaky tests, assertions renforcées).
- Amélioration de la robustesse de la migration de suppression de `deleted_at` sur `market_applications`. [#457](https://github.com/datagouv/passemarche/pull/457)
- Correction d'un problème avec le script de seed pour générer 1000 lots, qui passait maintenant par HTTP. [#436](https://github.com/datagouv/passemarche/pull/436)
- Ajout de la gem `aws-sdk-s3` pour le sandbox. [#442](https://github.com/datagouv/passemarche/pull/442)
- Correction d'un helper dans Lookbook. [#435](https://github.com/datagouv/passemarche/pull/435)
