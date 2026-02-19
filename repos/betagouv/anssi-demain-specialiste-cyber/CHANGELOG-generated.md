## Changelog : anssi-demain-specialiste-cyber (30 derniers jours)

### Résumé
Les dernières mises à jour du site "DemainSpécialisteCyber" se concentrent sur la correction de bugs, notamment liés à la soumission et à la création de jeux, ainsi que sur l'amélioration de la sécurité en mettant à jour certaines dépendances. Des ajustements ont également été apportés à l'interface utilisateur, notamment le remplacement d'un bloc par le kit de communication.

### Évolutions fonctionnelles
- Correction d'un bug empêchant le renvoi correct des résultats du cache en cas d'erreur Grist. (#62d1e8a)
- Désactivation du bouton de soumission du formulaire de jeu pour éviter des soumissions incorrectes. (#459449e, #560b534)
- Amélioration du message d'erreur affiché lors de la création d'un jeu pour une meilleure clarté. (#6bd6343)
- Remplacement du bloc "cyberenjeux" par le "kit de communication" pour mettre en avant de nouvelles ressources. (#70719da)
- Ajout de la section "kit de communication". (#812479f)

### Évolutions techniques
- Mise à jour de la dépendance `axios` vers la version 1.13.5 pour corriger des vulnérabilités de sécurité. (#8273d24)
- Mise à jour de la dépendance `fast-xml-parser` vers la version 5.3.6 pour corriger des vulnérabilités de sécurité. (#006d066)
- Correction de vulnérabilités de dépendances. (#1090414)

### Autres changements
- Suppression de logs d'investigation non nécessaires. (#505fb53)
- Ajout de logs temporaires pour faciliter le débogage des erreurs de création de jeu. (#b1572b0, #9ea2379)
- Amélioration du formattage Svelte dans l'environnement de développement VSCode. (#f4487af)
